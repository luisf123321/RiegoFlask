from flask import Blueprint

riego = Blueprint( 'riego' , __name__ , url_prefix='/riego')

from . import riego_route