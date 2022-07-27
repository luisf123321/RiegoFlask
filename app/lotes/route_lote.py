from . import lote

from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required)
from app.models.lote import Lote
from app.dao.lotes_dao import LotesDao
import json

@lote.route('finca/<int:finca_id>', methods=['GET'])
@jwt_required()
def buscarPorFinca(finca_id):
    lote = Lote(finca=finca_id)
    lotes = LotesDao.buscarPorFinca(lote)
    if lotes is None:
        return jsonify("no se encontro registro"),400
    else:
        print("*"*20)
        print(lotes)
        lotes_result = []
        for lote in lotes:
            lote = lote.replace("_","")
            lotes_result.append(json.loads(lote))
        return jsonify(lotes_result) ,200 

@lote.route('<int:id>', methods=['GET'])
@jwt_required()
def buscarPorId(id):
    lote = Lote(id=id)
    lote = LotesDao.buscarPorId(lote)
    if lote is None:
        return jsonify("no se encontro registro por id"),400
    else:
        lote = lote.replace("_","")
        return jsonify(json.loads(lote)) ,200  

@lote.route('', methods =['POST'])
@jwt_required()
def crear():
    nombre = request.json.get("nombre", None)
    area = request.json.get("area", None)
    latitud = request.json.get("latitud", None)
    longitud = request.json.get("longitud", None)
    altitud = request.json.get("altitud", None)
    finca_id = request.json.get("finca_id", None)
    finca = Lote(nombre=nombre,area=area,latitud=latitud,longitud=longitud,altitud=altitud,finca=finca_id)
    rows = LotesDao.insertar(finca)
    return jsonify({"code":200,"message":"Lote creado"}),200
    

    