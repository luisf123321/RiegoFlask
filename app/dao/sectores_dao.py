
from app.utilites.cursor_pool import CursorPool
from app.models.sectores import Sector
from app.utilites.logger_base import log

class SectoresDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM sectores ORDER BY id'
    _SELELCT_BY_LOTE = 'SELECT * FROM sectores WHERE sec_lotes=%s  ORDER BY id'
    _SELELCT_BY_CULTIVO = 'SELECT * FROM sectores WHERE sec_cultivo=%s  ORDER BY id'
    _INSERT = 'INSERT INTO sectores (sec_nombre, sec_lotes, sec_area, sec_latitud, sec_longitug, sec_altitud, sec_tipo_suelo,sec_cultivo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE sectores SET  sec_nombre=%s, sec_lotes=%s, sec_area=%s, sec_latitud=%s, sec_longitug=%s, sec_altitud=%s, sec_tipo_suelo=%s, sec_cultivo=%s WHERE id=%s'
    _DELETE = 'DELETE FROM sectores WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            sectores = []
            for registro in registros:
                sector = Sector(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7],registro[8])
                sectores.append(sector)
                print(sector)
            return sectores
    
    @classmethod
    def seleccionarByLotes(cls, lote):
        with CursorPool() as cursor:
            valores = (lote,)
            cursor.execute(cls._SELELCT_BY_LOTE,valores)
            registros = cursor.fetchall()
            if registros is None or registros == []:
                return None
            else:
                sectores = []
                for registro in registros:
                    sector = Sector(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7],registro[8])
                    sectores.append(sector)
                    print(sector)
                return sectores
    
    @classmethod
    def seleccionarByCultivo(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo,)
            cursor.execute(cls._SELELCT_BY_CULTIVO,valores)
            registros = cursor.fetchall()
            if registros is None or registros == []:
                return None
            else:
                sectores = []
                for registro in registros:
                    sector = Sector(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7],registro[8])
                    sectores.append(sector)
                    print(sector)
                return sectores
    
    @classmethod
    def eliminar(cls, sector):
        with CursorPool() as cursor:
            valores = (sector.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar sector, {sector}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,sector):
        with CursorPool() as cursor:
            valores = (sector.nombre, sector.lote, sector.area,sector.latitud,sector.longitud,sector.altitud,sector.suelo,sector.cultivo)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar sector, {sector}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, sector):
        with CursorPool() as cursor:
            valores = (sector.nombre, sector.lote, sector.area,sector.latitud,sector.longitud,sector.altitud,sector.suelo,sector.cultivo,sector.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar sector, {sector}')
            return cursor.rowcount