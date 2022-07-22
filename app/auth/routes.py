#from flask_login import login_user, login
from . import auth
from models.usuario import User
import pandas as pd 
from utilites import CursorPool
from werkzeug.security import generate_password_hash
from flask import request

@auth.route('/login', methods=['GET' , 'POST'])
def login():
    return "metodo login con Blueprint funcional"

@auth.route('signup', methods =['GET', 'POST'])
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
    consulta_usuario = Users.getUser(num_identificacion)
    #consulta_usuario = list(consulta_usuario)
    #consulta_usuario = consulta_usuario.to_dict()
    print(consulta_usuario)
    
    if len(consulta_usuario) == 0 :
        password_hash = generate_password_hash(password)
        Users.insertUser(username, apellido, num_identificacion, num_celular, direccion, nickname, password_hash,correo,tipo_identificacion)
        return username
    else:
        return "el usuario ya existe" 
    
