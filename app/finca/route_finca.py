from . import finca
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify

from app.models.finca import Finca
from app.dao.finca_dao import FincaDao
import json

@finca.route('user/<int:usuario_id>', methods=['GET'])
@jwt_required()
def buscarPorUsuario(usuario_id):
    finca = Finca(usuario=usuario_id)
    fincas = FincaDao.buscarFincaPorUsuario(finca)
    if fincas is None:
        return jsonify("no se encontro registro"),400
    else:
        print("*"*20)
        print(fincas)
        fincas_result = []
        for finca in fincas:
            finca = finca.replace("_","")
            fincas_result.append(json.loads(finca))
        return jsonify(fincas_result) ,200 


@finca.route('<int:id>', methods=['GET'])
@jwt_required()
def buscarPorId(id):
    finca = Finca(id=id)
    finca = FincaDao.buscarFincaPorId(finca)
    if finca is None:
        return jsonify("no se encontro registro por id"),400
    else:
        finca = finca.replace("_","")
        return jsonify(json.loads(finca)) ,200  


@finca.route('', methods =['POST'])
@jwt_required()
def crear():
    nombre = request.json.get("nombre", None)
    direccion = request.json.get("direccion", None)
    latitud = request.json.get("latitud", None)
    longitud = request.json.get("longitud", None)
    altitud = request.json.get("altitud", None)
    user_id = request.json.get("user_is", None)
    finca = Finca(nombre=nombre,direccion=direccion,latitud=latitud,longitud=longitud,altitud=altitud,usuario=user_id)

    rows = FincaDao.insertar(finca)
    return jsonify({"code":200,"message":"Finca creada"}),200
    

    