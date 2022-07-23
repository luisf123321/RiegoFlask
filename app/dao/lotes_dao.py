from utilites.cursor_pool import CursorPool
from models.lote import Lote
from utilites.logger_base import log

class LotesDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM lotes ORDER BY id'
    _INSERT = 'INSERT INTO lotes (lot_nombre, lot_finca, lot_area, lot_latitud, lot_longitug, lot_altitud) VALUES (%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE lotes SET  lot_nombre=%s, lot_finca=%s, lot_area=%s, lot_latitud=%s, lot_longitug=%s, lot_altitud=%s WHERE id=%s'
    _DELETE = 'DELETE FROM lotes WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            lotes = []
            for registro in registros:
                lote = Lote(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
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
    def insertar(cls,lote):
        with CursorPool() as cursor:
            valores = (lote.nombre, lote.finca, lote.area,lote.latitud,lote.longitud,lote.altitud)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar cultivo, {lote}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, lote):
        with CursorPool() as cursor:
            valores = (lote.nombre, lote.finca, lote.area,lote.latitud,lote.longitud,lote.altitud,lote.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar lote, {lote}')
            return cursor.rowcount