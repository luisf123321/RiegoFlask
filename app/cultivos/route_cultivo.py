from . import cultivo
import sys
from flask import request, jsonify
from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao


@cultivo.route('/id/<int:idcultivo>', methods=['POST'])
def login():
    return jsonify("cultivo")

@cultivo.route('/', methods =['POST'])
def signup():
    
    return jsonify({"code":400,"message":"El usuario ya existe"}),400