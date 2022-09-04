from . import lote

from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required)
from app.lotes.lote_logica import LoteLogica
import json

@lote.route('finca/<int:finca_id>', methods=['GET'])
@jwt_required()
def buscarPorFinca(finca_id):
    try:
        response = LoteLogica.buscarPorFinca(finca_id=finca_id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se encontraron  registros, vuelva intentar"})), 500

@lote.route('<int:id>', methods=['GET'])
@jwt_required()
def buscarPorId(id):
    try:
        response = LoteLogica.buscarPorId(id=id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se encontraron  registros, vuelva intentar"})), 500

@lote.route('', methods =['POST'])
@jwt_required()
def crear():
    try:
        data = request.json
        response = LoteLogica.crear(data=data)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500
    
@lote.route('<int:id>', methods =['PUT'])
@jwt_required()
def actualizar(id):
    try:
        data = request.json
        response = LoteLogica.actualizar(data=data, idLote=id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500