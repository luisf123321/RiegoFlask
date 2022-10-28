from app.utilites.cursor_pool import CursorPool
from app.models.muestra_suelo import MuestraSuelo
from app.utilites.logger_base import log
import json


class MuestraSueloDao:


    _SELELCT = 'SELECT * FROM muestra_suelo ORDER BY id'
    _SELELCT_BY_USUARIO = 'SELECT * FROM muestra_suelo WHERE usuario=%s  ORDER BY fecha'  
    _INSERT = 'INSERT INTO muestra_suelo (arena, limo, arcilla, tipo_suelo, usuario, fecha) VALUES (%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE muestra_suelo SET  arena=%s, limo=%s, arcilla=%s, tipo_suelo=%s, usuario=%s, fecha=%s WHERE id=%s'
    _DELETE = 'DELETE FROM muestra_suelo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            muestraSuelos = []
            for registro in registros:
                muestraSuelo = MuestraSuelo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],registro[6])
                muestraSuelos.append(muestraSuelo)
            return muestraSuelos
    
    @classmethod
    def seleccionarByUser(cls,usuario ):
        with CursorPool() as cursor:
            valores = (usuario,)
            cursor.execute(cls._SELELCT_BY_USUARIO, valores)
            registros = cursor.fetchall()
            loteMuestras = []
            for registro in registros:
                loteMuestra = MuestraSuelo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],registro[6])
                loteMuestras.append(loteMuestra)
                print(registro)
            return loteMuestras
    
    
    @classmethod
    def eliminar(cls, muestra):
        with CursorPool() as cursor:
            valores = (muestra.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar muestra, {muestra}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,muestra):
        with CursorPool() as cursor:
            valores = (muestra.arena, muestra.limo,muestra.arcilla,muestra.tipoSuelo,muestra.usuario,muestra.fecha )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar muestra, {muestra}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, muestra):
        with CursorPool() as cursor:
            valores = (muestra.arena, muestra.limo,muestra.arcilla,muestra.tipoSuelo,muestra.usuario,muestra.fecha, muestra.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar muestras, {muestra}')
            return cursor.rowcount