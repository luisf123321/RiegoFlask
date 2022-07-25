from . import finca

from flask import request, jsonify

from app.models.finca import Finca
from app.dao.finca_dao import FincaDao


@finca.route('finca/<int:usuario_id>', methods=['GET'])
def buscarPorUsuario(usuario_id):
    finca = Finca(usuario=usuario_id)
    fincas = FincaDao.buscarFincaPorUsuario(finca)
    if fincas is None:
        return jsonify(fincas),400
    else:
        print("*"*20)
        print(fincas)
        return jsonify(fincas),200 

@finca.route('finca/<int:id>', methods=['GET'])
def buscarPorId(id):
    finca = Finca(id=id)
    fincas = FincaDao.bus(finca)
    if fincas is None:
        return jsonify(fincas),400
    else:
        print("*"*20)
        print(fincas)
        return jsonify(fincas),200  

@finca.route('finca', methods =['POST'])
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
    

    