from flask import Blueprint

cultivo = Blueprint( 'cultivo' , __name__ , url_prefix='/cultivo')

from . import route_cultivo