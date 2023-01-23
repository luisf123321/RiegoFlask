
from flask import Blueprint

notificaciones = Blueprint('notificaciones', __name__,
                           url_prefix='/notificaciones')
from . import notificaciones_route