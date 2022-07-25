from app.utilites.cursor_pool import CursorPool
from app.models.lote import Lote
from app.utilites.logger_base import log
import json

class LotesDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM lotes ORDER BY id'
    _SELELCT_BY_ID = 'SELECT * FROM lotes WHERE id=%s'
    _SELELCT_BY_FINCA = 'SELECT * FROM lotes WHERE lot_finca=%s'
    _INSERT = 'INSERT INTO lotes (lot_nombre, lot_finca, lot_area, lot_latitud, lot_longitud, lot_altitud) VALUES (%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE lotes SET  lot_nombre=%s, lot_finca=%s, lot_area=%s, lot_latitud=%s, lot_longitud=%s, lot_altitud=%s WHERE id=%s'
    _DELETE = 'DELETE FROM lotes WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            lotes = []
            for registro in registros:
                lote = Lote(registro[0], registro[1], registro[2],
                            registro[3], registro[4], registro[5], registro[6])
                lotes.append(lote)
                print(lote)
            return lotes

    @classmethod
    def buscarPorId(cls, lote):
        with CursorPool() as cursor:
            valores = (lote.id,)
            cursor.execute(cls._SELELCT_BY_ID, valores)
            registro = cursor.fetchone()
            if registro is None:
                return None
            else:
                lote = Lote(registro[0], registro[1], registro[2],
                            registro[3], registro[4], registro[5], registro[6])
                return json.dumps(lote.__dict__)
            
    @classmethod
    def buscarPorFinca(cls, lote):
        with CursorPool() as cursor:
            valores = (lote.finca,)
            cursor.execute(cls._SELELCT_BY_FINCA, valores)
            registros = cursor.fetchall()
            if registros is None or registros == []:
                return None
            else:
                lotes = []
                for registro in registros:
                    lote = Lote(registro[0], registro[1], registro[2],
                                registro[3], registro[4], registro[5], registro[6])
                    lote = json.dumps(lote.__dict__)
                    lotes.append(lote)
                    print(lote)
                return lotes

    @classmethod
    def eliminar(cls, lote):
        with CursorPool() as cursor:
            valores = (lote.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar lote, {lote}')
            return cursor.rowcount

    @classmethod
    def insertar(cls, lote):
        with CursorPool() as cursor:
            valores = (lote.nombre, lote.finca, lote.area,
                       lote.latitud, lote.longitud, lote.altitud)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar lote, {lote}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, lote):
        with CursorPool() as cursor:
            valores = (lote.nombre, lote.finca, lote.area,
                       lote.latitud, lote.longitud, lote.altitud, lote.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar lote, {lote}')
            return cursor.rowcount
