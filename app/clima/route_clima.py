import json
from . import clima
import sys
from flask import request, jsonify
from app.clima.clima_logica import ClimaLogica

@clima.route('/coordenadas/<lat>/<long>')
def wheather(lat, long):
    try:
        print(float(lat), float(long))
        response = ClimaLogica.clima(lat=float(lat), long= float(long))
        return jsonify(response), 200
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500

@clima.route('/forecast/coordenadas/<lat>/<long>')
def forecast(lat, long):
    try:
        print(float(lat), float(long))
        response = ClimaLogica.forecast(lat=float(lat), long= float(long))
        return jsonify(response), 200
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


