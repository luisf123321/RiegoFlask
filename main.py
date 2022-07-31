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

CORS(app)


@app.route('/')
def hello_world():
    return jsonify("hello world")

if __name__ == '__main__':
    app.run(debug=True)
