from flask import Flask, request, jsonify, make_response , redirect , url_for
from flask_cors import CORS , cross_origin
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
import jwt
import datetime
import json
import os
import sys
import markdown
import datetime
from functools import wraps
from schema import Schema, And, Use, Optional
from pprint import pprint
import jsonpickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oasa.db'

cors = CORS(app)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    phone = db.Column(db.String(15)) #Support for international phone numbers
    hasReduced = db.Column(db.Boolean())

route_has_stations = db.Table('route_has_stations',
    db.Column('route_id', db.Integer, db.ForeignKey('route.id'), primary_key=True),
    db.Column('station_id', db.Integer, db.ForeignKey('station.id'), primary_key=True)
)

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    accesible = db.Column(db.Boolean())
    type = db.Column(db.String(5))
    def to_dict(self):
        r = {}
        r['public_id'] = self.public_id
        r['name'] = self.name
        r['lat'] = self.lat
        r['lng'] = self.lng
        r['accesible'] = self.accesible
        r['type'] = self.type
        routes_pid = []
        for route in self.routes:
            routes_pid.append(route.public_id)
        r['routes'] = routes_pid
        return r

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    start = db.Column(db.Integer,db.ForeignKey('station.id'))
    finish = db.Column(db.Integer,db.ForeignKey('station.id'))
    type = db.Column(db.String(6))
    firstRoute = db.Column(db.String())
    lastRoute = db.Column(db.String())
    frequency = db.Column(db.String())
    stations = db.relationship('Station', secondary=route_has_stations, lazy='subquery',
    backref=db.backref('routes', lazy=True))
    def to_dict(self):
        r = {}
        r['public_id'] = self.public_id
        r['name'] = self.name
        s = Station.query.get(self.start)
        f = Station.query.get(self.start)

        r['first_stop'] = s.public_id
        r['last_stop'] = f.public_id
        r['type'] = self.type
        r['first_route'] = self.firstRoute
        r['last_route'] = self.lastRoute
        r['frequency'] = self.frequency
        station_pids = []
        for station in self.stations:
            station_pids.append(station.public_id)
        r['stations'] = station_pids
        rr = {}
        rr['route'] = r
        return rr



db.create_all()
db.session.commit()

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

@app.route('/',methods=['GET'])
def hello():
    output = ''
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        output += markdown.markdown(content)
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

        return jsonify({'token' : token.decode('UTF-8'),'user': {'first_name' : user.name}})

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

    return jsonify({'user' : user_data})

@app.route('/routes',methods=['GET'])
def getRoutes():
    routes = Route.query.filter_by().all()
    routes_pid = []
    for route in routes:
        routes_pid.append(route.public_id)
    return jsonify({'routes' : routes_pid})
@app.route('/route/<public_id>',methods=['GET'])
def getRoute(public_id):
    route = Route.query.filter_by(public_id=public_id).first().to_dict()
    return jsonify(route)
@app.route('/stations',methods=['GET'])
def getStations():
    stations = Station.query.filter_by().all()
    stations_pid = []
    for station in stations:
        stations_pid.append(station.public_id)
    return jsonify({'stops' : stations_pid})

@app.route('/station/<public_id>',methods=['GET'])
def getStation(public_id):
    station = Station.query.filter_by(public_id=public_id).first().to_dict()
    return jsonify(station)


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


    new_user = User(
    public_id=str(uuid.uuid4()),
    name=data['name'],
    password=hashed_password,
    first_name=data['first_name'],
    last_name=data['last_name'],
    email=data['email'],
    phone=data['phone'],
    hasReduced=False,
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'New user created!'})

if __name__ == '__main__':
    app.run(debug=True)
