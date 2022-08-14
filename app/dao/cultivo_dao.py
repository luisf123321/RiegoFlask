

from app.utilites.cursor_pool import CursorPool
from app.models.cultivo import Cultivo
from app.utilites.logger_base import log
import json
import datetime
class CultivoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM cultivo ORDER BY id'
    _SELECT_BY_USER = 'SELECT * FROM cultivo WHERE cul_user=%s '
    _SELECT_BY_ID = 'SELECT * FROM cultivo WHERE id=%s '
    _INSERT = 'INSERT INTO cultivo (cul_nombre, cul_tipo_cul, cul_fecha_inicio, cul_fecha_final, cul_estado,cul_user) VALUES (%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE cultivo SET  cul_nombre=%s, cul_tipo_cul=%s, cul_fecha_inicio=%s, cul_fecha_final=%s, cul_estado=%s,cul_user=%s WHERE id=%s'
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
    def buscarPorUsuario(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.user,)
            cursor.execute(cls._SELECT_BY_USER,valores)
            registros = cursor.fetchall()
            if registros is None or registros == []:
                return None
            else:
                cultivos = []
                for registro in registros:
                    fecha_inicio = registro[3]
                    fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')   
                    fecha_fin = registro[4]
                    fecha_fin=fecha_fin.strftime('%Y-%m-%d')    
                    cultivo = Cultivo(registro[0], registro[1], registro[2], fecha_inicio, fecha_fin, registro[5], registro[6])
                    cultivo = json.dumps(cultivo.__dict__)
                    cultivos.append(cultivo)
                    print(cultivo)
                return cultivos
    
    @classmethod
    def buscarPorId(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.id,)
            cursor.execute(cls._SELECT_BY_ID,valores)
            registro = cursor.fetchone()
            if registro is None:
                return None
            else:
                print("cultivo")
                print(registro)
                fecha_inicio = registro[3]
                fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')   
                fecha_fin = registro[4]
                fecha_fin=fecha_fin.strftime('%Y-%m-%d')              
                cultivo = Cultivo(registro[0], registro[1], registro[2], fecha_inicio, fecha_fin, registro[5], registro[6])
                print(cultivo.__dict__)   
                cultivo = json.dumps(cultivo.__dict__)
                print(cultivo)
                return cultivo
               
    
    @classmethod
    def eliminar(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar cultivo, {cultivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.cultivoNombre, cultivo.tipoCultivo,cultivo.fechaInicio,cultivo.fechaFinal,cultivo.cultivoEstado,cultivo.user )
            print("valores")
            print(valores)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar cultivo, {cultivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.cultivoNombre, cultivo.tipoCultivo,cultivo.fechaInicio,cultivo.fechaFinal,cultivo.cultivoEstado,cultivo.user, cultivo.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar cultivo, {cultivo}')
            return cursor.rowcount