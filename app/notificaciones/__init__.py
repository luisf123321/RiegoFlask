
from flask import Blueprint

notificaciones = Blueprint('notificaciones', __name__,
                           url_prefix='/notificacionbes')
from . import notificaciones_route