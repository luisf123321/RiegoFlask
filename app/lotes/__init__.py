from flask import Blueprint

lote = Blueprint( 'lote' , __name__ , url_prefix='/lote')

from . import route_lote