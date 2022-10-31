from . import sectores
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify
import json
from app.sectores.sectores_logica import SectoresLogica

@sectores.route('/lote/<int:lote_id>', methods=['GET'])
@jwt_required()
def buscarPorLote(lote_id):
    try:
        response = SectoresLogica.obtenerSectoresByLotes(lote=lote_id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500

@sectores.route('/cultivo/<int:cultivo_id>', methods=['GET'])
@jwt_required()
def buscarPorCultivo(cultivo_id):
    try:
        print(cultivo_id)
        response = SectoresLogica.obtenerSectoresByCultivo(cultivo=cultivo_id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500