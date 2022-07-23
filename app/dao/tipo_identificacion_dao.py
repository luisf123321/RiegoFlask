

from utilites.cursor_pool import CursorPool
from models.tipo_identificacion import TipoIdentificacion
from utilites.logger_base import log

class TipoIdentificacionDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM tipo_dispositivo ORDER BY id'
    _INSERT = 'INSERT INTO tipo_dispositivo (tip_ident_nombre, tip_ident_descripcion) VALUES (%s,%s)'
    _UPDATE = 'UPDATE tipo_dispositivo SET  tip_ident_nombre=%s, tip_ident_descripcion=%s WHERE id=%s'
    _DELETE = 'DELETE FROM tipo_dispositivo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            tipoDispositivos = []
            for registro in registros:
                tipoDispositivo = TipoDispositivo(registro[0], registro[1], registro[2])
                tipoDispositivos.append(tipoDispositivo)
                print(tipoDispositivo)
            return tipoDispositivos
    
    @classmethod
    def eliminar(cls, tipoDispositivo):
        with CursorPool() as cursor:
            valores = (tipoDispositivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar tipo dispositivo, {tipoDispositivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,tipoDispositivo):
        with CursorPool() as cursor:
            valores = (tipoDispositivo.categoria, tipoDispositivo.caracteristica)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar tipo dispositivo, {tipoDispositivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, tipoDispositivo):
        with CursorPool() as cursor:
            valores = (tipoDispositivo.categoria, tipoDispositivo.caracteristica,tipoDispositivo.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar tipo dispositivo, {tipoDispositivo}')
            return cursor.rowcount