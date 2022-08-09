from . import riego
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify

from app.models.admin_riego import AdminRiego
from app.models.tipo_riego import TipoRiego


from app.dao.tipo_riego_dao import TipoRiegoDao
from app.dao.admin_riego_dao import AdminRiegoDao
import json


@riego.route('sector/<int:sector>', methods=['GET'])
@jwt_required()
def buscarPorSector(sector):
    print(sector)
    admin = AdminRiego(sector=sector)
    riegos = AdminRiegoDao.buscarSector(admin)
    if riegos is None:
        return jsonify("no se encontro registro"),400
    else:
        print("*"*20)
        print(riegos)
        admin_riegos_result = []
        for riego in riegos:
            riego = riego.replace("_","")
            admin_riegos_result.append(json.loads(riego))
        return jsonify(admin_riegos_result) ,200 


@riego.route('<int:id>', methods=['GET'])
@jwt_required()
def buscarPorLote(id):
    return "hello"


@riego.route('tipo', methods=['GET'])
@jwt_required()
def buscarTodos():
    print("tipo")
    registros = TipoRiegoDao.seleccionarTodos()
    if registros is None:
        return jsonify("no se encontro registro"),400
    else:
        print("*"*20)
        print(registros)
        tipos_riego_result = []
        for tipoRiego in registros:
            tipoRiego = tipoRiego.replace("_","")
            tipos_riego_result.append(json.loads(tipoRiego))
        return jsonify(tipos_riego_result) ,200 


