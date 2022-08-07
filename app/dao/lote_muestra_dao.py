from app.utilites.cursor_pool import CursorPool
from app.models.lote_muestra import LoteMuestra
from app.utilites.logger_base import log
import json


class LoteMuestraDao:


    _SELELCT = 'SELECT * FROM lote_muestras ORDER BY id'    
    _INSERT = 'INSERT INTO lote_muestras (arena, limo, arcilla, lote, tipo_suelo) VALUES (%(float)s,%(float)s,%(float)s,%(int)s,%(int)s)'
    _UPDATE = 'UPDATE lote_muestras SET  arena=%s, limo=%s, arcilla=%s, lote=%s, tipo_suelo=%s WHERE id=%s'
    _DELETE = 'DELETE FROM lote_muestras WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            loteMuestras = []
            for registro in registros:
                loteMuestra = LoteMuestra(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                loteMuestras.append(loteMuestra)
                print(registro)
            return loteMuestras
    
    
    @classmethod
    def eliminar(cls, loteMuestra):
        with CursorPool() as cursor:
            valores = (loteMuestra.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar loteMuestra, {loteMuestra}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,loteMuestra):
        with CursorPool() as cursor:
            valores = (loteMuestra.arena, loteMuestra.limo,loteMuestra.arcilla,loteMuestra.lote,loteMuestra.tipo_suelo )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar loteMuestra, {loteMuestra}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, loteMuestra):
        with CursorPool() as cursor:
            valores = (loteMuestra.arena, loteMuestra.limo,loteMuestra.arcilla,loteMuestra.lote,loteMuestra.tipo_suelo, loteMuestra.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar loteMuestras, {loteMuestra}')
            return cursor.rowcount