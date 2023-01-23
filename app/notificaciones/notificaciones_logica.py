from app.dao.notificaciones_dao import NotificacionesDao
from app.models.notificaciones import Notificaciones

import json


class NotificacionesLogica:
    @classmethod
    def buscarByUsuario(cls, usuario):
        notificaciones = NotificacionesDao.buscarByUser(usuario=usuario)
        if notificaciones is None:
            return dict({"code": 400, "message": "Sectores no encontrado"})
        else:
            notificaciones_result = []
            for notificacion in notificaciones:
                notificacion = json.dumps(notificacion.__dict__)
                notificacion = notificacion.replace("_", "")
                notificaciones_result.append(json.loads(notificacion))
            return dict({"code": 200, "message": "notificaciones encontrados", "notificaciones": notificaciones_result})
