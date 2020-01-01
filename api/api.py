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

@app.route('/categories',methods=['GET'])
#@token_required
def showCategories():
    sem.acquire()
    cur = dbItems.cursor()
    cur.execute("SELECT * FROM Category")
    categories =cur.fetchall()
    cur.close()
    sem.release()
    output = []
    for value in categories:
        data = {}
        data['id'] = value['idCategory']
        data['name'] = value['Name']
        output.append(data)
    print(output)
    return jsonify({"data" : output}) , 200

@app.route('/categories/<id>',methods=['GET'])
@token_required
def showCategory(current_user,id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    sem.acquire()
    cur = dbItems.cursor()
    sql = "SELECT Name FROM Category cat WHERE cat.idCategory = %s " % (id)
    cur.execute(sql)
    category = cur.fetchone()
    cur.close()
    sem.release()
    return jsonify({"Id" : id , "Name" : category['Name']})
@app.route('/categories',methods=['POST'])
@token_required
def addCategory(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    data = request.get_json()
    name = data['name']
    sql = "INSERT INTO AuctionsSite.Category VALUES (NULL,'%s');" % (name)
    sem.acquire()
    cur = dbItems.cursor()
    cur.execute(sql)
    dbItems.commit()
    cur.close()
    sem.release()
    return jsonify({"Message" : "Added new Category" , "Data" : data})


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
@app.route('/user/pending', methods=['GET'])
@token_required
def showPendingUsers(current_user):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    users = User.query.all()

    output = []

    for user in users:
        if user.pending is False:
            continue
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['first_name'] = user.first_name
        user_data['last_name'] = user.last_name

        output.append(user_data)

    return jsonify({'users' : output})
@app.route('/user/pending/<user_public_id>', methods=['PUT'])
@token_required
def acceptUser(current_user, user_public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=user_public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})
    if user.pending == False :
        return jsonify({'message' : 'User not pending !'})


    print(user.id)
    sem.acquire()
    sqlAddID = "INSERT INTO User VALUES ({})".format(user.id)
    cursor = dbItems.cursor()
    cursor.execute(sqlAddID)
    dbItems.commit()
    cursor.close()
    sem.release()

    sqlCreateSeller = "INSERT INTO Seller VALUES (NULL,0,{},0)".format(user.id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlCreateSeller)
    dbItems.commit()
    cursor.close()
    sem.release()

    sqlCreateBidder = "INSERT INTO Bidder VALUES (NULL,0,'Adanon 7',{},0)".format(
    user.id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlCreateBidder)
    dbItems.commit()
    cursor.close()
    sem.release()

    user.pending = False
    dbUsers.session.commit()

    return jsonify({'message' : 'The user has been accepted!'}),200


@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user.admin = True
    dbUsers.session.commit()

    return jsonify({'message' : 'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    dbUsers.session.delete(user)
    dbUsers.session.commit()

    return jsonify({'message' : 'The user has been deleted!'})

# To add a new auction to the database first we check that the categories
# requested are correct . Then we find the seller id associated with the loged in
# user. We insert to the Item database and we get the generated id(auto_increment)
# then we add the categories for the item in the has_Categories table.
@app.route('/auction',methods=['POST'])
@token_required
def createAuction(current_user):
    user = User.query.filter_by(public_id=current_user.public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})
    data = request.get_json()
    #print(data)


    name = data['name']
    if not data['name'] or not data['firstBid'] or not data['ends'] :
        return jsonify({'message' : 'missing data!'}),422
    desc = data['description']
    categories = data['categories']

    for category in categories:
        sem.acquire()
        sqlCheckCategory = "SELECT * FROM Category where idCategory = {}".format(category)
        cursor = dbItems.cursor()
        cursor.execute(sqlCheckCategory)
        result = cursor.fetchall()
        print(result,file=sys.stderr)
        if cursor.rowcount == 0:
            cursor.close()
            sem.release()
            return jsonify({'message' : 'Category not found '})
        cursor.close()
        sem.release()
    if not data['buyPrice']:
        buy = 'null'
    else :
        buy = data['buyPrice']
    first = data['firstBid']
    location = data['location'][0]
    print(location)
    address = data['address']
    starts = data['starts']
    starts_obj = datetime.datetime.strptime(starts, '%Y-%m-%dT%H:%M')
    print(data)

    ends = data['ends']
    ends_obj = datetime.datetime.strptime(ends, '%Y-%m-%dT%H:%M')

    sqlSellerId = "SELECT idSeller FROM Seller where User_UserID = {}".format(user.id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlSellerId)
    sid = cursor.fetchone()
    cursor.close()
    sem.release()
    #country = data['country']
    #city = data['city']
    sqlAddItem = "INSERT INTO Item VALUES (NULL,'{}',{},{},{},0,{},{},'{}','{}','{}',{},'{}',false,false)".format(name,first,buy,first,location['lat'],location['lng'],address,starts_obj.strftime('%Y-%m-%d %H:%M:%S'),ends_obj.strftime('%Y-%m-%d %H:%M:%S'),sid['idSeller'],desc)
    print(sqlAddItem)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlAddItem)
    newid = cursor.lastrowid
    dbItems.commit()
    cursor.close()
    sem.release()
    for category in categories:
        sqlAddhasCategory = "insert into has_Categories values (NULL,{},{})".format(category,newid)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlAddhasCategory)
        dbItems.commit()
        cursor.close()
        sem.release()
    return jsonify({'message':'Created succesfully','id' : newid})

@app.route('/auction/<int:id>',methods=['POST'])
@token_required
def addImages(current_user,id) :
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file part')
            return jsonify({'message' : 'no file part'}) , 401
        for file in request.files.getlist('file'):
            print(file)
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                print('no selected file')
                return jsonify({'message' : 'no selected file'}) , 401
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = app.config['UPLOAD_FOLDER'] + str(id) + '/' + filename

                if not os.path.exists(os.path.dirname(path)):
                    try:
                        os.makedirs(os.path.dirname(path))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file.save(path)
                uploaded_image = im.upload_image(path, title="Uploaded with PyImgur")
                print(uploaded_image.link)
                sqlAddImage = "INSERT INTO Image VALUES (NULL,'{}')".format(uploaded_image.link)
                sem.acquire()
                cursor = dbItems.cursor()
                cursor.execute(sqlAddImage)
                newid = cursor.lastrowid
                dbItems.commit()
                cursor.close()
                sem.release()

                sem.acquire()
                sqlAddhasImage = "INSERT INTO has_Images values (NULL,{},{})".format(id,newid)
                cursor = dbItems.cursor()
                cursor.execute(sqlAddhasImage)
                dbItems.commit()
                cursor.close()
                sem.release()

        return jsonify({'message' : 'success upload'}) , 200


@app.route('/auction/<int:id>',methods=['GET'])
@token_required
def showAuction(current_user,id):
    sqlGetCategories = "select Category.Name from Category , has_Categories where \
    has_Categories.Item_ItemID = {} and \
    has_Categories.Category_idCategory = Category.idCategory ".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetCategories)
    result = cursor.fetchall()
    cursor.close()
    sem.release()
    categoryNames = []
    for value in result:
        categoryNames.append(value['Name'])
    sqlGetBids = "select idBid , price from has_Bids , Bid where \
    has_Bids.Item_ItemID = {} and \
    has_Bids.Bid_idBid = Bid.idBid".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetBids)
    bids = cursor.fetchall()
    cursor.close()
    sem.release()

    sqlGetItem = "select * from Item where Item.ItemID = {}".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetItem)
    result = cursor.fetchone()
    cursor.close()
    sem.release()

    sqlGetImages = "select Image.idImage , Image.name from has_Images , Image where has_Images.Item_ItemID = {} and Image.idImage = has_Images.Image_idImage".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetImages)
    images = cursor.fetchall()
    cursor.close()
    sem.release()

    sqlGetSeller = "select Seller.User_UserID , Seller.Rating , Seller.Number_of_Ratings from Seller , Item where Item.Seller_idSeller = Seller.idSeller and Item.ItemID = {}".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetSeller)
    seller = cursor.fetchone()
    cursor.close()
    sem.release()
    id = seller['User_UserID']
    name = User.query.filter_by(id=id).first().name
    seller['name'] = name
    isSeller = False
    if id == current_user.id:
        isSeller = True
    return jsonify({'Categories' : categoryNames,'Images' : images , 'Item':result ,'Bids' : bids ,
    'Seller' : seller , 'isSeller' : isSeller})

@app.route('/auction/user/finished',methods=['GET'])
@token_required
def retrieveUserFinished(current_user):
    sellerid = current_user.id

    sqlGetAllAuctions = "Select ItemID, Name , Buy_Price , Currently ,Ends , Description from Item , Seller where Item.Seller_idSeller = Seller.idSeller and Seller.User_UserID = {} and Item.hasEnded = true and Item.Seller_idSeller = Seller.idSeller".format(sellerid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetAllAuctions)
    items = cursor.fetchall()
    cursor.close()
    sem.release()
    for val in items:
        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetImages = "select name from Image , has_Images where has_Images.Item_ItemID = {} and has_Images.Image_idImage = Image.idImage ".format(val['ItemID'])
        cursor.execute(sqlGetImages)
        images = cursor.fetchall()
        val['images'] = images
        cursor.close()
        sem.release()

        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetCategories = "select Category.idCategory , Category.Name from Category , has_Categories , Item where has_Categories.Item_ItemID = {} and has_Categories.Category_idCategory = Category.idCategory and Item.ItemID = {} ".format(val['ItemID'],val['ItemID'])
        cursor.execute(sqlGetCategories)
        categories = cursor.fetchall()
        val['categories'] = categories
        cursor.close()
        sem.release()


    return jsonify(items)
@app.route('/auction/user/ongoing',methods=['GET'])
@token_required
def retrieveUserAuctions(current_user):
    sellerid = current_user.id

    sqlGetAllAuctions = "Select ItemID, Name , Buy_Price , Currently ,Ends , Description from Item , Seller where Item.Seller_idSeller = Seller.idSeller and Seller.User_UserID = {} and Item.Started < NOW() and Item.Ends > NOW() and Item.hasEnded = false".format(sellerid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetAllAuctions)
    items = cursor.fetchall()
    cursor.close()
    sem.release()
    for val in items:
        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetImages = "select name from Image , has_Images where has_Images.Item_ItemID = {} and has_Images.Image_idImage = Image.idImage ".format(val['ItemID'])
        cursor.execute(sqlGetImages)
        images = cursor.fetchall()
        val['images'] = images
        cursor.close()
        sem.release()

        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetCategories = "select Category.idCategory , Category.Name from Category , has_Categories , Item where has_Categories.Item_ItemID = {} and has_Categories.Category_idCategory = Category.idCategory and Item.ItemID = {} ".format(val['ItemID'],val['ItemID'])
        cursor.execute(sqlGetCategories)
        categories = cursor.fetchall()
        val['categories'] = categories
        cursor.close()
        sem.release()


    return jsonify(items)

@app.route('/auction/user/upcoming',methods=['GET'])
@token_required
def retrieveUpcomingAuctions(current_user):
    sellerid = current_user.id

    sqlGetAllAuctions = "Select ItemID, Name , Buy_Price , Currently ,Ends , Description from Item , Seller where Item.Seller_idSeller = Seller.idSeller and Seller.User_UserID = {} and Item.Started > NOW()".format(sellerid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetAllAuctions)
    items = cursor.fetchall()
    cursor.close()
    sem.release()
    for val in items:
        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetImages = "select name from Image , has_Images where has_Images.Item_ItemID = {} and has_Images.Image_idImage = Image.idImage ".format(val['ItemID'])
        cursor.execute(sqlGetImages)
        images = cursor.fetchall()
        val['images'] = images
        cursor.close()
        sem.release()
        sem.acquire()

        cursor = dbItems.cursor()
        sqlGetCategories = "select Category.idCategory , Category.Name from Category , has_Categories , Item where has_Categories.Item_ItemID = {} and has_Categories.Category_idCategory = Category.idCategory and Item.ItemID = {} ".format(val['ItemID'],val['ItemID'])
        cursor.execute(sqlGetCategories)
        categories = cursor.fetchall()
        val['categories'] = categories
        cursor.close()
        sem.release()


    return jsonify(items)

@app.route('/auction/user/purchases',methods=['GET'])
@token_required
def retrievePurchases(current_user):
    buyerid = current_user.id

    sqlGetAuctions = '''
    select Item.ItemID , Item.Name , Item.Buy_Price , Item.Currently ,Item.Ends , Item.Description
    from Item , has_Bids , Bid , Bidder where
    Item.ItemID = has_Bids.Item_ItemID and
    has_Bids.Bid_idBid = Bid.idBid and
    Bidder.idBidder = Bid.Bidder_idBidder and
    Bidder.User_UserID = {} and
    Item.Currently = Bid.price
    '''.format(buyerid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetAuctions)
    items = cursor.fetchall()
    cursor.close()
    sem.release()
    for val in items:
        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetImages = "select name from Image , has_Images where has_Images.Item_ItemID = {} and has_Images.Image_idImage = Image.idImage ".format(val['ItemID'])
        cursor.execute(sqlGetImages)
        images = cursor.fetchall()
        val['images'] = images
        cursor.close()
        sem.release()
        sem.acquire()

        cursor = dbItems.cursor()
        sqlGetCategories = "select Category.idCategory , Category.Name from Category , has_Categories , Item where has_Categories.Item_ItemID = {} and has_Categories.Category_idCategory = Category.idCategory and Item.ItemID = {} ".format(val['ItemID'],val['ItemID'])
        cursor.execute(sqlGetCategories)
        categories = cursor.fetchall()
        val['categories'] = categories
        cursor.close()
        sem.release()


    return jsonify(items)


@app.route('/auction',methods=['GET'])
def get_auctions():
    sqlGetAllAuctions = "Select ItemID, Name , Buy_Price , Currently ,Ends ,Description from Item where Item.Ends > NOW() and Item.hasEnded = false and Item.Started < now()"
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetAllAuctions)
    items = cursor.fetchall()
    cursor.close()
    sem.release()
    for val in items:
        sem.acquire()
        cursor = dbItems.cursor()
        sqlGetImages = "select name from Image , has_Images where has_Images.Item_ItemID = {} and has_Images.Image_idImage = Image.idImage ".format(val['ItemID'])
        cursor.execute(sqlGetImages)
        images = cursor.fetchall()
        val['images'] = images
        cursor.close()
        sem.release()
        sem.acquire()

        cursor = dbItems.cursor()
        sqlGetCategories = "select Category.idCategory , Category.Name from Category , has_Categories , Item where has_Categories.Item_ItemID = {} and has_Categories.Category_idCategory = Category.idCategory and Item.ItemID = {} ".format(val['ItemID'],val['ItemID'])
        cursor.execute(sqlGetCategories)
        categories = cursor.fetchall()
        val['categories'] = categories
        cursor.close()
        sem.release()


    return jsonify(items)
@app.route('/auction/<int:id>',methods=['PATCH'])
@token_required
def update_auction(current_user,id):
    data = request.get_json()
    sellerid = current_user.id
    sqlGetItemID = "Select ItemID from Item , Seller where Item.Seller_idSeller = Seller.idSeller and Seller.User_UserID = {} and Item.ItemID = {}".format(sellerid,id)

    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetItemID)
    result = cursor.fetchall()
    if not result :
        return jsonify({'message':'cant update auction not belonging to user'}),401
    cursor.close()
    sem.release()
    if 'name' in data:
        newname = data['name']
        sqlUpdate = "UPDATE Item SET Name = '{}' where Item.ItemID = {}".format(newname,id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()

    if 'buyprice' in data:
        newprice = data['name']
        sqlUpdate = "UPDATE Item SET Buy_Price = {} where Item.ItemID = {}".format(newprice,id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()
    if 'firstbid' in data:
        newfbid = data['firstbid']
        sqlUpdate = "UPDATE Item SET First_Bid = {} where Item.ItemID = {}".format(newfbid,id)
        sem.acquire()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()
    if 'address' in data:
        newaddress = data['address']
        sqlUpdate = "UPDATE Item SET Address = '{}' where Item.ItemID = {}".format(newaddress,id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()
    if 'lat' in data:
        newlat = data['lat']
        sqlUpdate = "UPDATE Item SET Lat = {} where Item.ItemID = {}".format(newlat,id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()
    if 'lng' in data:
        newlng = data['lng']
        sqlUpdate = "UPDATE Item SET Lng = {} where Item.ItemID = {}".format(newlng,id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()
    if 'description' in data:
        newdesc = data['description']
        sqlUpdate = "UPDATE Item SET Description = '{}' where Item.ItemID = {}".format(newdesc,id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdate)
        cursor.close()
        sem.release()
    if 'imageschanged' in data:
        if data['imageschanged']:
                sqlRemoveImages = "DELETE Image, has_Images FROM Image INNER JOIN has_Images WHERE Image.idImage=has_Images.Image_idImage AND has_Images.Item_ItemID = {}".format(id)
                sem.acquire()
                cursor = dbItems.cursor()
                cursor.execute(sqlRemoveImages)
                cursor.close()
                sem.release()
    if 'categories' in data :
        newcategories = data['categories']
        print(newcategories)
        sqlRemoveCategories = "DELETE FROM has_Categories WHERE has_Categories.Item_ItemID = {}".format(id)
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlRemoveCategories)
        cursor.close()
        sem.release()
        for category in newcategories:
            sqlUpdate = "insert into has_Categories values (NULL,{},{})".format(category,id)
            sem.acquire()
            cursor = dbItems.cursor()
            cursor.execute(sqlUpdate)
            cursor.close()
            sem.release()

    return jsonify({'message' : 'success'})

@app.route('/auction/<int:id>/bid',methods=['PATCH'])
@token_required
def bid(current_user,id) :
    data = request.get_json()
    sqlGetItemPrice = "select Currently , hasEnded , Buy_Price from Item where ItemID = {}".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetItemPrice)
    result = cursor.fetchone()
    cursor.close()
    sem.release()
    currentprice = result['Currently']
    buyprice = result['Buy_Price']
    hasEnded = result['hasEnded']
    if hasEnded:
        return jsonify({'message' : 'auction has finished'}) , 401


    uid = current_user.id
    print(uid)
    sqlGetBidderID = "select idBidder from Bidder , User where Bidder.User_UserID = {}".format(uid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetBidderID)
    result = cursor.fetchone()
    cursor.close()
    sem.release()

    bidderid = result['idBidder']
    data = request.get_json()
    print(request)
    print(data)
    price = int(data['price'])
    if price < currentprice:
        return jsonify({'message':'bid is less than current highest'}) , 401
    if buyprice :
        if price >= buyprice :
            sqlCreateThread = '''
            insert into thread
            select null , Item.Name , now() , Bidder.idBidder , Item.Seller_idSeller , Item.ItemID
            from Item , Bidder
            where Item.ItemID = {} and
            Bidder.idBidder = {}
            '''.format(id , bidderid)
            sem.acquire()
            cursor = dbItems.cursor()
            cursor.execute(sqlCreateThread)
            dbItems.commit()
            cursor.close()
            sem.release()
            sqlSetHasEnded = '''
            update Item
            set Item.hasEnded = true
            where Item.ItemID = {}
            '''.format(id)
            sem.acquire()
            cursor = dbItems.cursor()
            cursor.execute(sqlSetHasEnded)
            dbItems.commit()
            cursor.close()
            sem.release()



    sqlCreateBid = "insert into Bid values (NULL,{},{})".format(price,bidderid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlCreateBid)
    bidid = cursor.lastrowid
    dbItems.commit()
    cursor.close()
    sem.release()

    sqlAddBid = "insert into has_Bids values (NULL,{},{})".format(id,bidid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlAddBid)
    dbItems.commit()
    cursor.close()
    sem.release()

    sem.acquire()
    sqlUpdatePrice = "update Item set Currently = {} , Number_of_Bids = Number_of_Bids + 1 where Item.ItemID = {} ".format(price,id)
    cursor = dbItems.cursor()
    cursor.execute(sqlUpdatePrice)
    dbItems.commit()
    cursor.close()
    sem.release()
    return jsonify({'message' : 'success'})

@app.route('/auction/<int:id>/rate',methods=['POST'])
@token_required
def rateSeller(current_user,id) :
    data = request.get_json()
    rating = int(data['rating'])
    if rating < 0 or rating > 5:
        return jsonify({'message' : 'incorrect rating'}),400

    sqlGetSellerID = '''
    select Seller_idSeller
    from Item
    where Item.ItemID = {}
    '''.format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetSellerID)
    result = cursor.fetchone()
    cursor.close()
    sem.release()

    idSeller = result['Seller_idSeller']

    sqlUpdateRating = '''
    update Seller
    set Rating = ((Rating*Number_of_Ratings) + {})/(Number_of_Ratings + 1) ,
    Number_of_Ratings = Number_of_Ratings + 1
    where Seller.idSeller = {}
    '''.format(rating,idSeller)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlUpdateRating)
    dbItems.commit()
    cursor.close()
    sem.release()

    sqlUpdateItem = '''
    update Item
    set hasRating = true
    where Item.ItemID = {}
    '''.format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlUpdateItem)
    dbItems.commit()
    cursor.close()
    sem.release()

    return jsonify({'message' : 'submitted rating succesfully'})

# We want to add a message to our Message table
# a message has a type and text
@app.route('/messages/<int:id>',methods=["PATCH"])
@token_required
def addMessage(current_user,id):
    data = request.get_json()
    type = data['type']
    data = data['data']
    # first we get the participant id of the seller
    # next we get the participant id of the buyer ,
    # we check if the sender is seller or buyer
    # and we add the new message to the message table
    sqlGetGroupID = "select * from thread as t where t.Item_ItemID = {}".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetGroupID)
    result = cursor.fetchone()
    cursor.close()
    sem.release()
    threadid = result['idthread']

    sqlGetParticipants = '''
    select Seller.User_UserID , Bidder.User_UserID , Seller.idSeller , Bidder.idBidder
    from thread , Seller , Bidder
    where thread.idthread = {} and
    thread.Seller_idSeller = Seller.idSeller and
    thread.Bidder_idBidder = Bidder.idBidder
    '''.format(threadid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetParticipants)
    result = cursor.fetchone()
    cursor.close()
    sem.release()
    print(result,current_user.id)
    uidSeller = result['User_UserID']
    uidBuyer = result['Bidder.User_UserID']

    fromSeller = 'false'
    fromBuyer = 'false'
    if uidSeller == current_user.id:
        fromSeller = 'true'
    elif uidBuyer == current_user.id:
        fromBuyer = 'true'
    else :
        return jsonify({'message' : 'not auth to access messages'}) , 401

    sqlAddMessage = '''
    insert into message
    values (null , '{}' , '{}' , now() , false , {} , {} , {})
    '''.format(type,data,threadid,fromSeller,fromBuyer)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlAddMessage)
    dbItems.commit()
    cursor.close()
    sem.release()

    return jsonify({'message' : 'added message to thread'})

@app.route('/messages/<int:id>',methods=['GET'])
@token_required
def getMessages(current_user,id):
    sqlGetGroupID = "select * from thread as t where t.Item_ItemID = {}".format(id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetGroupID)
    result = cursor.fetchone()
    cursor.close()
    sem.release()
    threadid = result['idthread']

    sqlGetMessages = '''
    select m.fromSeller , m.fromBuyer , m.type , m.data , m.created , m.isRead
    from message as m
    where m.thread_idthread = {}
    order by m.created asc
    '''.format(threadid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetMessages)
    messages = cursor.fetchall()
    cursor.close()
    sem.release()

    sqlGetParticipants = '''
    select Seller.User_UserID , Bidder.User_UserID , Seller.idSeller , Bidder.idBidder
    from thread , Seller , Bidder
    where thread.idthread = {} and
    thread.Seller_idSeller = Seller.idSeller and
    thread.Bidder_idBidder = Bidder.idBidder
    '''.format(threadid)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetParticipants)
    result = cursor.fetchone()
    cursor.close()
    sem.release()
    print(result,current_user.id)
    uidSeller = result['User_UserID']
    uidBuyer = result['Bidder.User_UserID']
    isSeller = True
    if uidSeller == current_user.id:
        mypid = result['idSeller']
        otherpid = result['idBidder']
    elif uidBuyer == current_user.id:
        otherpid = result['idSeller']
        mypid = result['idBidder']
        isSeller = False
    else :
        return jsonify({'message' : 'not auth to access messages'}) , 401

    return jsonify({'data':messages,'isSeller':isSeller,'other':otherpid})

#function executed by scheduled job
def updateDB():
    sqlGetExpiredAuctions = '''
    select ItemID
    from Item
    where hasEnded = false AND
    Ends < now()
    '''
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlGetExpiredAuctions)
    items = cursor.fetchall()
    cursor.close()
    sem.release()
    bidder = []
    for item in items:
        sqlUpdateItem = '''
        update Item
        set hasEnded = true
        where ItemID = {} and
        hasEnded = false
        '''.format(item['ItemID'])
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlUpdateItem)
        dbItems.commit()
        cursor.close()
        sem.release()

        sqlGetHighBidder = '''
        select Item.ItemID , Bidder.idBidder , Bid.price
        from Item , has_Bids , Bid , Bidder where
        Item.ItemID = {} and
        Item.ItemID = has_Bids.Item_ItemID and
        has_Bids.Bid_idBid = Bid.idBid and
        Bidder.idBidder = Bid.Bidder_idBidder
        group by Bid.price , Item.ItemID , Bidder.idBidder , Bid.price
        '''.format(item['ItemID'])
        sem.acquire()
        cursor = dbItems.cursor()
        cursor.execute(sqlGetHighBidder)
        result = cursor.fetchone()
        cursor.close()
        sem.release()
        if not result:
            pass
        else :
            bidder.append(result)
            sqlCreateThread = '''
            insert into thread
            select null , Item.Name , now() , Bidder.idBidder , Item.Seller_idSeller , Item.ItemID
            from Item , Bidder
            where Item.ItemID = {} and
            Bidder.idBidder = {}
            '''.format(item['ItemID'] , result['idBidder'])
            sem.acquire()
            cursor = dbItems.cursor()
            cursor.execute(sqlCreateThread)
            dbItems.commit()
            cursor.close()
            sem.release()


    print(items,bidder,str(datetime.datetime.now()))



if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(func=updateDB, trigger='interval', id='job', seconds=30)
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
