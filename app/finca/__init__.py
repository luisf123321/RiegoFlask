from flask import Blueprint

finca = Blueprint( 'finca' , __name__ , url_prefix='/finca')

from . import route_fincas