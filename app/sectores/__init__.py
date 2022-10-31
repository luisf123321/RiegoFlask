from flask import Blueprint

sectores = Blueprint( 'sectores' , __name__ , url_prefix='/sectores')

from . import sectores_route