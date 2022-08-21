#from flask_login import login_user, login
from pydoc import doc
from . import auth
import sys
import os
import pandas as pd 
from werkzeug.security import generate_password_hash,check_password_hash
from flask import request, jsonify
#sys.path.append(os.path.abspath('..'))
from app.models.usuario import User
from app.dao.usuario_dao import UsuarioDao
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from app.extensions import jwt


@auth.route('login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    usuario = User(user=username,password=password)    
    consulta_usuario = UsuarioDao.buscarUserName(usuario)
    print(consulta_usuario)
    if consulta_usuario is None or not check_password_hash(consulta_usuario.password, password):
        return jsonify("Wrong username or password"), 401
    else:
        user = {
            "id": consulta_usuario.id,
            "apellido": consulta_usuario.apellido,
            "nombre": consulta_usuario.nombre,
            "username": consulta_usuario.user
        }
        access_token = create_access_token(identity=user)
        #refresh_token = create_refresh_token(identity=user)
        #return jsonify(access_token=access_token, refresh_token=refresh_token)
        return jsonify(access_token=access_token),200
        #return jsonify({"code":400,"message":"El usuario ya existe"}),400

@auth.route('signup', methods =['POST'])
def signup():
    username = request.json.get("username", None)
    apellido = request.json.get("apellido", None)
    num_identificacion = request.json.get("num_identificacion", None)
    num_celular = request.json.get("num_celular", None)
    direccion = request.json.get("direccion", None)
    nickname = request.json.get("nickname", None)
    password = request.json.get("password", None)
    correo = request.json.get("correo", None)
    tipo_identificacion = int(request.json.get("tipo_identificacion", None))
    usuario = User( nombre= nickname, apellido=apellido,documento=num_identificacion,celular=num_celular,direccion=direccion,user=username,password=password,correo=correo,tipoIdentificacion=tipo_identificacion)
    
    consulta_usuario = UsuarioDao.buscarPorDocumento(usuario)
    
    if consulta_usuario is None :
        password_hash = generate_password_hash(password)
        usuario.password = password_hash
        rows = UsuarioDao.insertar(usuario)
        return jsonify({"code":200,"message":"Usuario creado"}),200
    else:
         return jsonify({"code":400,"message":"El usuario ya existe"}),400

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user


@auth.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    current_user = get_jwt_identity()
    return jsonify(
        nombre=current_user['nombre'],
        apellido = current_user['apellido'],
        id = current_user['id'],
        username = current_user['username']
    )


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return identity
