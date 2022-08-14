from . import cultivo
import sys
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required)
from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao
import json

@cultivo.route('/user/<int:idUser>', methods=['GET'])
@jwt_required()
def buscarPoruser(idUser):
    cultivo = Cultivo(user=idUser)
    cultivos = CultivoDao.buscarPorUsuario(cultivo=cultivo)
    if cultivos is None:
        return jsonify("no se encontro registro"),400
    else:
        print(cultivos)
        cultivos_result = []
        for cultivo in cultivos:
            cultivo = cultivo.replace("_","")
            cultivos_result.append(json.loads(cultivo))
        return jsonify(cultivos_result) ,200 

@cultivo.route('/<int:idCultivo>', methods=['GET'])
@jwt_required()
def buscarPorId(idCultivo):
    cultivo = Cultivo(id=idCultivo)
    cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
    if cultivo is None:
        return jsonify("no se encontro registro por id"),400
    else:
        cultivo = cultivo.replace("_","")
        return jsonify(json.loads(cultivo)) ,200  

@cultivo.route('/', methods =['POST'])
@jwt_required()
def crear():
    nombre = request.json.get("nombre", None)
    tipo_cultivo = request.json.get("tipoCultivo", None)
    fecha_inicio = request.json.get("fechaInicio", None)
    fecha_final = request.json.get("fechaFinal", None)
    estado = request.json.get("estado", None)
    user_id = request.json.get("user_id", None) 
    cultivo = Cultivo(cultivoNombre=nombre,tipoCultivo=tipo_cultivo,fechaInicio=fecha_inicio,fechaFinal=fecha_final,cultivoEstado=estado,user=user_id)  
    CultivoDao.insertar(cultivo=cultivo)
    return jsonify({"code":200,"message":"cultivo creado"}),200

@cultivo.route('/<int:idCultivo>', methods =['PUT'])
@jwt_required()
def actualizar(idCultivo):
    cultivo = Cultivo(id=idCultivo)
    cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
    if cultivo is None:
        return jsonify("no se encontro registro"),400
    else:
        nombre = request.json.get("nombre", None)
        tipo_cultivo = request.json.get("tipoCultivo", None)
        fecha_inicio = request.json.get("fechaInicio", None)
        fecha_final = request.json.get("fechaFinal", None)
        estado = request.json.get("estado", None)
        user_id = request.json.get("user_id", None) 
        cultivo = Cultivo(cultivoNombre=nombre,tipoCultivo=tipo_cultivo,fechaInicio=fecha_inicio,fechaFinal=fecha_final,cultivoEstado=estado,user=user_id,id=idCultivo)  
        CultivoDao.actualizar(cultivo=cultivo)
        return jsonify({"code":200,"message":"cultivo actualizado"}),200