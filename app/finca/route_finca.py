from . import finca
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify

from app.finca.finca_logica import FincaLogica

@finca.route('user/<int:usuario_id>', methods=['GET'])
@jwt_required()
def buscarPorUsuario(usuario_id):
    try:
        response = FincaLogica.buscarPorUsuario(usuario_id=usuario_id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500



@finca.route('<int:id>', methods=['GET'])
@jwt_required()
def buscarPorId(id):
    try:
        response = FincaLogica.buscarPorId(idFinca=id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@finca.route('', methods =['POST'])
@jwt_required()
def crear():
    try:
        data = request.json
        response = FincaLogica.crearFinca(data=data)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500

@finca.route('<int:id>', methods =['PUT'])
@jwt_required()
def actualizar(id):
    try:
        data = request.json
        response = FincaLogica.actualizarFinca(data=data,idfinca=id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500
    

    