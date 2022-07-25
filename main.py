from flask import Flask, request, jsonify
#from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from app.models.usuario import User
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
    #usuario = Users.getUsers()
    #print(type(jsonify(usuario.to_json(orient='columns'))))  
    return jsonify("hello world")

if __name__ == '__main__':
    app.run(debug=True)
