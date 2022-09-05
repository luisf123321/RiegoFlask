import json
from . import clima
import sys
from flask import request, jsonify
from app.clima.clima_logica import ClimaLogica

@clima.route('/coordenadas')
def clima():
    try:
        response = ClimaLogica.clima()
        return jsonify(response), 200
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


