from . import cultivo
import sys
from flask import request, jsonify
from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao


@cultivo.route('/id/<int:idcultivo>', methods=['POST'])
def buscar():
    return jsonify("cultivo")

@cultivo.route('/', methods =['POST'])
def crear():    
    return jsonify({"code":400,"message":"El usuario ya existe"}),400