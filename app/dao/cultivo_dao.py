

from utilites.cursor_pool import CursorPool
from models.cultivo import Cultivo
from utilites.logger_base import log

class CultivoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM cultivo ORDER BY id'
    _INSERT = 'INSERT INTO cultivo (cul_nombre, cul_tipo_cul, cul_lotes, cul_fecha_inicio, cul_fecha_final, cul_estado) VALUES (%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE cultivo SET  cul_nombre=%s, cul_tipo_cul=%s, cul_lotes=%s, cul_fecha_inicio=%s, cul_fecha_final=%s, cul_estado=%s WHERE id=%s'
    _DELETE = 'DELETE FROM cultivo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            cultivos = []
            for registro in registros:
                cultivo = Cultivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                cultivos.append(cultivo)
                print(registro)
            return cultivos
    
    @classmethod
    def eliminar(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar persona, {cultivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.cultivoNombre, cultivo.tipoCultivo, cultivo.cultivoLote,cultivo.fechaInicio,cultivo.fechaFinal,cultivo.cultivoEstado )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar persona, {cultivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.cultivoNombre, cultivo.tipoCultivo, cultivo.cultivoLote,cultivo.fechaInicio,cultivo.fechaFinal,cultivo.cultivoEstado, cultivo.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar persona, {cultivo}')
            return cursor.rowcount