from flask import Blueprint

mod1 = Blueprint( 'mod1' , __name__ , url_prefix='/mod1')

#from . import routes