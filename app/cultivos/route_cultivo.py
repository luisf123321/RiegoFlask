from . import cultivo
import sys
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required)
from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao
from app.dao.tipo_cultivo_dao import TipoCultivoDao
from app.models.tipo_cultivo import TipoCultivo
import json
from app.email.body import BodyEmail
from app.email.send import SendEmail
from app.cultivos.cultivo_ligica import CultivoLogica


@cultivo.route('/user/<int:idUser>', methods=['GET'])
@jwt_required()
def buscarPoruser(idUser):
    cultivo = Cultivo(user=idUser)
    cultivos = CultivoDao.buscarPorUsuario(cultivo=cultivo)
    if cultivos is None:
        return jsonify("no se encontro registro"), 400
    else:
        print(cultivos)
        cultivos_result = []
        for cultivo in cultivos:
            cultivo = cultivo.replace("_", "")
            cultivos_result.append(json.loads(cultivo))
        return jsonify(cultivos_result), 200


@cultivo.route('/<int:idCultivo>', methods=['GET'])
@jwt_required()
def buscarPorId(idCultivo):
    try:
        print("********************** eliminar cultivos")
        print(idCultivo)
        response = CultivoLogica.buscarCultivoPorId(id=idCultivo)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@cultivo.route('/<int:idCultivo>', methods=['DELETE'])
@jwt_required()
def eliminarPorId(idCultivo):
    try:
        print("********************** eliminar cultivos")
        print(idCultivo)
        response = CultivoLogica.eliminarCultivo(id=idCultivo)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@cultivo.route('/', methods=['POST'])
@jwt_required()
def crear():
    nombre = request.json.get("nombre", None)
    tipo_cultivo = request.json.get("tipoCultivo", None)
    fecha_inicio = request.json.get("fechaInicio", None)
    fecha_final = request.json.get("fechaFinal", None)
    estado = request.json.get("estado", None)
    user_id = request.json.get("user_id", None)
    cultivo = Cultivo(cultivoNombre=nombre, tipoCultivo=tipo_cultivo,
                      fechaInicio=fecha_inicio, fechaFinal=fecha_final, cultivoEstado=estado, user=user_id)
    CultivoDao.insertar(cultivo=cultivo)
    html = BodyEmail.bodyToRegister()
    SendEmail.send(html, 'encisolf901@gmail.com',
                   "Welcome to riego application")
    return jsonify({"code": 200, "message": "cultivo creado"}), 200


@cultivo.route('/<int:idCultivo>', methods=['PUT'])
@jwt_required()
def actualizar(idCultivo):
    cultivo = Cultivo(id=idCultivo)
    cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
    if cultivo is None:
        return jsonify("no se encontro registro"), 400
    else:
        nombre = request.json.get("nombre", None)
        tipo_cultivo = request.json.get("tipoCultivo", None)
        fecha_inicio = request.json.get("fechaInicio", None)
        fecha_final = request.json.get("fechaFinal", None)
        estado = request.json.get("estado", None)
        user_id = request.json.get("user_id", None)
        cultivo = Cultivo(cultivoNombre=nombre, tipoCultivo=tipo_cultivo, fechaInicio=fecha_inicio,
                          fechaFinal=fecha_final, cultivoEstado=estado, user=user_id, id=idCultivo)
        CultivoDao.actualizar(cultivo=cultivo)
        return jsonify({"code": 200, "message": "cultivo actualizado"}), 200


@cultivo.route('/tipos', methods=['GET'])
@jwt_required()
def tipocultivos():
    tipos = TipoCultivoDao.seleccionarTodos()
    if tipos is None:
        return jsonify("no se encontro registro"), 400
    else:
        print(tipos)
        tipos_cultivos_result = []
        for tipo in tipos:
            tipo = tipo.replace("_", "")
            tipos_cultivos_result.append(json.loads(tipo))
        return jsonify(tipos_cultivos_result), 200
