from flask import Blueprint

clima = Blueprint( 'clima' , __name__ , url_prefix='/clima')

from . import route_clima