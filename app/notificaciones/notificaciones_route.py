from . import notificaciones
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify
import json
from app.notificaciones.notificaciones_logica import NotificacionesLogica


@notificaciones.route('/usuario/<int:user_id>', methods=['GET'])
@jwt_required()
def buscarPorUsuario(user_id):
    try:
        response = NotificacionesLogica.buscarByUsuario(usuario=user_id)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500
