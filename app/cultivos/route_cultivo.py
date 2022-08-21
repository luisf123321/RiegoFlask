from . import cultivo
import sys
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required)
from app.email.body import BodyEmail
from app.email.send import SendEmail
from app.cultivos.cultivo_ligica import CultivoLogica


@cultivo.route('/user/<int:idUser>', methods=['GET'])
@jwt_required()
def buscarPoruser(idUser):
    try:
        response = CultivoLogica.buscarCultivoPorUser(idUser=idUser)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@cultivo.route('/<int:idCultivo>', methods=['GET'])
@jwt_required()
def buscarPorId(idCultivo):
    try:
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
    try:
        data = request.json
        response = CultivoLogica.crearCultivo(data=data)
        html = BodyEmail.bodyToRegister()
        SendEmail.send(html, 'encisolf901@gmail.com',
                    "Welcome to riego application")  
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500

@cultivo.route('/<int:idCultivo>', methods=['PUT'])
@jwt_required()
def actualizar(idCultivo):
    try:
        data = request.json
        response = CultivoLogica.actualizarCultivo(data=data,idCultivo=idCultivo)
        html = BodyEmail.bodyToRegister()
        SendEmail.send(html, 'encisolf901@gmail.com',
                    "Welcome to riego application")  
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@cultivo.route('/tipos', methods=['GET'])
@jwt_required()
def tipocultivos():
    try:
        response = CultivoLogica.tipocultivos()
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500
