from . import riego
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify

from app.models.admin_riego import AdminRiego
from app.models.tipo_riego import TipoRiego


from app.dao.tipo_riego_dao import TipoRiegoDao
from app.dao.admin_riego_dao import AdminRiegoDao
import json


@riego.route('user/<int:lote>', methods=['GET'])
@jwt_required()
def buscarPorLote(lote):
    return "hello"


@riego.route('user/<int:lote>', methods=['GET'])
@jwt_required()
def buscarPorLote(lote):
    return "hello"