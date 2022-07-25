from utilites.cursor_pool import CursorPool
from models.finca import Finca
from utilites.logger_base import log
import json

class FincaDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM finca ORDER BY id'
    _SELELCT_BY_USUARIO = 'SELECT * FROM finca WHERE fin_usuario=%s'
    _SELELCT_BY_ID = 'SELECT * FROM finca WHERE id=%s'
    _INSERT = 'INSERT INTO finca (fin_nombre, fin_direccion, fin_latitud, fin_longitud, fin_altitud, fin_usuario) VALUES (%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE finca SET  fin_nombre=%s, fin_direccion=%s, fin_latitud=%s, fin_longitud=%s, fin_altitud=%s, fin_usuario=%s WHERE id=%s'
    _DELETE = 'DELETE FROM finca WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            fincas = []
            for registro in registros:
                finca = Finca(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                fincas.append(finca)
                print(finca)
            return 
    
    @classmethod
    def buscarFincaPorUsuario(cls,finca):
        with CursorPool() as cursor:
            valores = (finca.usuario,)
            cursor.execute(cls._SELELCT_BY_USUARIO,valores)
            registros = cursor.fetchall()
            if registros is None or registros == []:
                return None
            else:
                fincas = []
                for registro in registros:
                    finca = Finca(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                    fincas.append(json.dumps(finca.__dict__))
                    print(finca)
                return fincas
    
    @classmethod
    def buscarFincaPorId(cls,finca):
        with CursorPool() as cursor:
            valores = (finca.id,)
            cursor.execute(cls._SELELCT_BY_ID,valores)
            registro = cursor.fetchone()
            if registro is None:
                return None
            else:
                finca = Finca(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                return json.dumps(finca.__dict__)
    
    @classmethod
    def eliminar(cls, finca):
        with CursorPool() as cursor:
            valores = (finca.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar finca, {finca}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,finca):
        with CursorPool() as cursor:
            valores = (finca.nombre, finca.direccion, finca.latitud,finca.longitud,finca.altitud,finca.usuario )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar finca, {finca}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, finca):
        with CursorPool() as cursor:
            valores = (finca.nombre, finca.direccion, finca.latitud,finca.longitud,finca.altitud,finca.usuario,finca.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar cultivo, {finca}')
            return cursor.rowcount