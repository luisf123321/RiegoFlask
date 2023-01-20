from . import riego
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify
from app.riego.riego_logica import Riegologica





@riego.route('sector/<int:sector>', methods=['GET'])
@jwt_required()
def buscarPorSector(sector):
    try:        
        response = Riegologica.buscarPorSector( sector=sector)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500



@riego.route('tipo', methods=['GET'])
@jwt_required()
def buscarTodos():
    try:
        
        response = Riegologica.obtenerTipoDeRiego()
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@riego.route('tipodispositivo', methods=['GET'])
@jwt_required()
def buscarPorDispositivos():
    try:        
        response = Riegologica.obtenerTipoDeDispositivo()
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500

@riego.route('admin', methods=['POST'])
@jwt_required()
def guardarAdminRiego():
    try:
        data = request.json
        response = Riegologica.crearAdminRiego(data=data)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@riego.route('dispositivo', methods=['POST'])
@jwt_required()
def guardarDispositivo():
    try:
        data = request.json
        response = Riegologica.crearDispositivo(data=data)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@riego.route('dispositivo/usuario/<int:usuario>', methods=['GET'])
@jwt_required()
def buscarDispositivosByUsuario(usuario):
    try:        
        response = Riegologica.obtenerDispositivoByUsuario(usuario)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@riego.route('dispositivo/sector/<int:sector>', methods=['GET'])
@jwt_required()
def buscarDispositivosBySectores(sector):
    try:        
        response = Riegologica.obtenerDispositivoBysectore(sector=sector)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@riego.route('admin/usuario/<int:usuario>', methods=['GET'])
@jwt_required()
def buscarAdminRiegoByUsuario(usuario):
    try:        
        response = Riegologica.obtenerAdminRiegoByUsuario(usuario=usuario)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500
