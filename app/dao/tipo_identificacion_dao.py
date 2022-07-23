

from utilites.cursor_pool import CursorPool
from models.tipo_identificacion import TipoIdentificacion
from utilites.logger_base import log

class TipoIdentificacionDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM tipo_identificacion ORDER BY id'
    _INSERT = 'INSERT INTO tipo_identificacion (tip_ident_nombre, tip_ident_descripcion) VALUES (%s,%s)'
    _UPDATE = 'UPDATE tipo_identificacion SET  tip_ident_nombre=%s, tip_ident_descripcion=%s WHERE id=%s'
    _DELETE = 'DELETE FROM tipo_identificacion WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            tipoIdentificacions = []
            for registro in registros:
                tipoIdentificacion = TipoIdentificacion(registro[0], registro[1], registro[2])
                tipoIdentificacions.append(tipoIdentificacion)
                print(tipoIdentificacion)
            return tipoIdentificacions
    
    @classmethod
    def eliminar(cls, tipoIdentificacion):
        with CursorPool() as cursor:
            valores = (tipoIdentificacion.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar tipo identificacion, {tipoIdentificacion}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,tipoIdentificacion):
        with CursorPool() as cursor:
            valores = (tipoIdentificacion.nombre, tipoIdentificacion.descripcion)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar tipo identificacion, {tipoIdentificacion}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, tipoIdentificacion):
        with CursorPool() as cursor:
            valores = (tipoIdentificacion.nombre, tipoIdentificacion.descripcion,tipoIdentificacion.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar tipo identificacion, {tipoIdentificacion}')
            return cursor.rowcount