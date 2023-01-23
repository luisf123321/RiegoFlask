

from app.utilites.cursor_pool import CursorPool
from app.models.notificaciones import Notificaciones
from app.utilites.logger_base import log


class CultivoDao:

    '''
    DAO --> Data Access Object
    '''
    _SELECT_BY_USER = 'SELECT * FROM notificaciones WHERE usuario=%s '
    _SELECT_BY_ID = 'SELECT * FROM notificaciones WHERE id=%s '
    _INSERT = 'INSERT INTO notificaciones (usuario, mensaje, estado, fecha_origen, fecha_vista) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE notificaciones SET  usuario=%s, mensaje=%s, estado=%s, fecha_origen=%s, fecha_vista=%s WHERE id=%s'
    _DELETE = 'DELETE FROM notificaciones WHERE id=%s'

    @classmethod
    def buscarByUser(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario,)
            cursor.execute(cls._SELECT_BY_USER, valores)
            registros = cursor.fetchall()
            notificaciones = []
            for registro in registros:
                notificacion = Notificaciones(registro[0], registro[1], registro[2],
                                              registro[3], registro[4], registro[5])
                notificaciones.append(notificacion)
            return notificaciones

    @classmethod
    def buscarById(cls, id):
        with CursorPool() as cursor:
            valores = (id,)
            cursor.execute(cls._SELECT_BY_ID, valores)
            registro = cursor.fetchone()
            if registro is None:
                return None
            else:
                notificacion = Notificaciones(registro[0], registro[1], registro[2],
                                              registro[3], registro[4], registro[5])
                return notificacion

    @classmethod
    def eliminar(cls, id):
        with CursorPool() as cursor:
            valores = (id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar notificacion, {id}')
            return cursor.rowcount

    @classmethod
    def insertar(cls, notificacion):
        with CursorPool() as cursor:
            valores = (notificacion.usuario,
                       notificacion.mensaje, notificacion.estado, notificacion.fechaOrigen, notificacion.fechaVista)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar notificacion, {notificacion}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, notificacion):
        with CursorPool() as cursor:
            valores = (notificacion.usuario,
                       notificacion.mensaje, notificacion.estado, notificacion.fechaOrigen, notificacion.fechaVista, notificacion.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar notificacion, {notificacion}')
            return cursor.rowcount
