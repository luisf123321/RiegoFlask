from flask import Flask, request, jsonify
#from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from app.models import Users
from app.auth.routes import signup



from app import create_app


app = create_app()
#app.config['MONGO_URI'] = 'mongodb://localhost/riego2'
#app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@neivaroutes.ymunc.mongodb.net/Riego?retryWrites=true&w=majority'

#mongo = PyMongo(app)

CORS(app)

jwt = JWTManager(app)

@app.route('/')
def hello_world():
    #usuario = Users.getUser(str(1022))
    usuario = Users.getUsers()
    print(type(jsonify(usuario.to_json(orient='columns'))))  
    return (usuario.to_json(orient='columns'))

"""
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


"""

if __name__ == '__main__':
    app.run(debug=True)
