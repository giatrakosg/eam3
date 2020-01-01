from flask import Flask, request, jsonify, make_response , redirect , url_for
from flask_cors import CORS , cross_origin
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
import jwt
import datetime
import pymysql
import json
import os
import sys
import markdown
import datetime
from functools import wraps
from imgurpython import ImgurClient
import pyimgur
import threading
from schema import Schema, And, Use, Optional
from pprint import pprint
from flask_apscheduler import APScheduler

sem = threading.Semaphore()

UPLOAD_FOLDER = '/tmp/'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

client_id = 'e4d20924ee4c9f1'
client_secret = 'f61fd060aaeac98748b387826d44f841d901c3bd'

im = pyimgur.Imgur(client_id)

cors = CORS(app)

dbUsers = SQLAlchemy(app)
dbItems =pymysql.connect(user='root',password='root',database='AuctionsSite',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)

class User(dbUsers.Model):
    id = dbUsers.Column(dbUsers.Integer, primary_key=True)
    public_id = dbUsers.Column(dbUsers.String(50), unique=True)
    name = dbUsers.Column(dbUsers.String(50),unique=True)
    password = dbUsers.Column(dbUsers.String(80))
    admin = dbUsers.Column(dbUsers.Boolean)
    pending = dbUsers.Column(dbUsers.Boolean)
    first_name = dbUsers.Column(dbUsers.String(50))
    last_name = dbUsers.Column(dbUsers.String(50))
    email = dbUsers.Column(dbUsers.String(50),unique=True)
    phone = dbUsers.Column(dbUsers.String(15)) #Support for international phone numbers
    # length 15
    tin = dbUsers.Column(dbUsers.String(9)) # AFM = TIN (Tax Identification number)
    # We restrict to 9 digits
    location = dbUsers.Column(dbUsers.Float())
    # when the user was registered
    register = dbUsers.Column(dbUsers.Date())


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/hello',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file part')
            return jsonify({'message' : 'no file part'}) , 401
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no selected file')
            return jsonify({'message' : 'no selected file'}) , 401
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'message' : 'success upload'}) , 200


@app.route('/',methods=['GET'])
def hello():
    output = """<!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" type="text/css" href="static/style.css">
                """

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        output += markdown.markdown(content)
        output += """
        </head>

        <body>
        """
        return output
@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=90)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8'),'first_name' : user.first_name , 'last_name' : user.last_name})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


# Shows all registered users
# if the current user is the admin.Else
# gets the public id of the current user
@app.route('/user', methods=['GET'])
@token_required
def showUsers(current_user):

    if current_user.admin:
        users = User.query.all()

        output = []

        for user in users:
            if user.pending is True:
                continue
            user_data = {}
            user_data['name'] = user.name
            user_data['email'] = user.email
            user_data['first_name'] = user.first_name
            user_data['last_name'] = user.last_name
            output.append(user_data)

        return jsonify({'users' : output})
    user = User.query.filter_by(public_id=current_user.public_id).first()
    if not user :
        return jsonify({'message' : 'No user found!'})
    user_data = {}
    user_data['name'] = user.name
    user_data['public_id'] = user.public_id
    return jsonify({'user' : user_data})



@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'No user found!'})
    if current_user.public_id != public_id and current_user.admin == False:
        return jsonify({'message' : 'Unauthorized user'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['admin'] = user.admin
    user_data['first_name'] = user.first_name
    user_data['last_name'] = user.last_name
    user_data['email'] = user.email
    user_data['phone'] = user.phone
    user_data['location'] = user.location
    user_data['tin'] = user.tin


    return jsonify({'user' : user_data})

@app.route('/user', methods=['POST'])
def addUserRequest():
    data = request.get_json()
    print(data,file=sys.stderr)
    hashed_password = generate_password_hash(data['password'], method='sha256')

    uName = User.query.filter_by(name=data['name']).all()
    if len(uName) > 0 :
        return jsonify({'message' : 'User already exists!'}),400
    uEmail = User.query.filter_by(email=data['email']).all()
    if len(uEmail) > 0 :
        return jsonify({'message' : 'Email already exists!'}),400


    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False,
    pending=True,first_name=data['first_name'],last_name=data['last_name'],email=data['email'],
    phone=data['phone'],tin=data['tin'],location=data['location'])
    dbUsers.session.add(new_user)
    dbUsers.session.commit()
    return jsonify({'message' : 'New user created!'})

if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(func=updateDB, trigger='interval', id='job', seconds=30)
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
