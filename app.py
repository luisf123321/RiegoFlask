from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from datetime import timedelta
import pymongo



app = Flask(__name__)
#app.config['MONGO_URI'] = 'mongodb://localhost/riego2'
#app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@neivaroutes.ymunc.mongodb.net/Riego?retryWrites=true&w=majority'
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=4)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)


client = pymongo.MongoClient("mongodb+srv://admin:admin@neivaroutes.ymunc.mongodb.net/Riego?retryWrites=true&w=majority")
db = client.Riego.users

#mongo = PyMongo(app)

CORS(app)

jwt = JWTManager(app)
#db = mongo.db.users
#dbcultivo = mongo.db.cultivos
#dblotes = mongo.db.lotes
dbcultivo = client.Riego.cultivos
dblotes = client.Riego.lotes
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users', methods = ['POST'])
def createUser():
    print(request.json)
    d = request.json
    id = db.insert(d)
    return jsonify(str(ObjectId(id)))


@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for user in db.find():
        users.append({
            "_id": str(ObjectId(user['_id'])),
            "nombre": user['nombre'],
            "apellido": user['apellido'],
        })
    print(users)

    return jsonify(users)


@app.route('/user/<id>',methods=['GET'])
def getUser(id):
    user = db.find_one({"_id": ObjectId(id)})
    return jsonify(
        {
            "nombre":user['nombre'],
            "apellido": user['apellido']
        }
    )


@app.route('/user/<id>',methods=['DELETE'])
def deleteUser(id):
    user = db.delete_one({"_id": ObjectId(id)})
    return jsonify(
        {
            "message":"ok"
        }
    )


@app.route('/user/<id>', methods=['PUT'])

def updateUser(id):
    user = db.update_one({"_id": ObjectId(id)}, {"$set": {
        "nombre": request.json['nombre'],
        "apellido":request.json['apellido'],
        "edad": request.json['edad']
    }})
    return jsonify(
        {
            "message": "update"
        }
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    userfind = db.find_one({'username': username})
    if not userfind or not userfind['password'] == password:
        return jsonify("Wrong username or password"), 401
    user = {
        "id": str(ObjectId(userfind['_id'])),
        "apellido": userfind['apellido'],
        "nombre": userfind['nombre'],
        "username": userfind['username']
    }
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user['id']


@app.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    print(current_user)
    return jsonify(
        nombre=current_user['nombre'],
        apellido = current_user['apellido'],
        email = current_user['email'],
        username = current_user['username']
    )


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.find_one({"_id": ObjectId(identity)})


@app.route("/cultivos", methods=["GET"])
@jwt_required()
def getCultivos():
    iduser = current_user['_id']
    cultivos = []
    for cultivo in dbcultivo.find({"iduser":iduser}):
        cultivos.append({
            "_id": str(ObjectId(cultivo['_id'])),
            "cultivo":cultivo['cultivo'],
            "fecha":cultivo['fecha']
        })

    print(iduser)
    return jsonify({"cultivos":cultivos})


@app.route("/cultivos", methods=["POST"])
@jwt_required()
def creatCiltivo():
    iduser = current_user['_id']
    cultivo = request.json
    cultivo['iduser'] = iduser
    cultivo = dbcultivo.insert(cultivo)
    return  jsonify({"_id":str(ObjectId(cultivo))})


@app.route("/Lotes", methods=["POST"])
@jwt_required()
def creatLote():
    iduser = current_user['_id']
    Lotes = request.json
    Lotes['iduser'] = iduser
    Lote = dblotes.insert(Lotes)
    return  jsonify({"_id":str(ObjectId(Lote))})


@app.route("/Lotes", methods=["GET"])
@jwt_required()
def getLotes():
    iduser = current_user['_id']
    lotes = []
    for lote in dblotes.find({"iduser":iduser}):
        lotes.append({
            "_id": str(ObjectId(lote['_id'])),
            "lote":lote['lote'],
            "fecha":lote['fecha'],
            "area":lote['area']
        })

    print(iduser)
    return jsonify({"lotes":lotes})


if __name__ == '__main__':
    app.run()
