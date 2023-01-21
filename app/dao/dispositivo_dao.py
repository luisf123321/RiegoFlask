
from app.utilites.cursor_pool import CursorPool
from app.models.dispositivo import Dispositivo
from app.utilites.logger_base import log
import json
class DispositivoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM dispositivo ORDER BY id'
    _SELELCT_BY_SECTOR = 'SELECT * FROM dispositivo WHERE dis_sectores = %s ORDER BY id'
    _SELELCT_BY_USUARIO = 'SELECT dis_sectores.id, dis.dis_nombre, dis.dis_tipo,dis.dis_modelo,dis.dis_sectores,dis.dis_estado  FROM dispositivo as dis INNER JOIN sectores as sec ON sec.id = dis.dis_sectores INNER JOIN lotes as lot ON sec.sec_lotes = lot.id INNER JOIN finca as fin ON fin.id = lot.lot_finca  WHERE fin.fin_usuario=%s  ORDER BY dis.id'
    _INSERT = 'INSERT INTO dispositivo (dis_nombre, dis_tipo, dis_modelo, dis_sectores, dis_estado) VALUES (%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE dispositivo SET  dis_nombre=%s, dis_tipo=%s, dis_modelo=%s, dis_sectores=%s, dis_estado=%s WHERE id=%s'
    _DELETE = 'DELETE FROM dispositivo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            dispositivos = []
            for registro in registros:
                dispositivo = Dispositivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                dispositivos.append(dispositivo)
                print(registro)
            return dispositivos
    
    @classmethod
    def seleccionarBySectores(cls,sector):
        with CursorPool() as cursor:
            valores = (sector,)
            cursor.execute(cls._SELELCT_BY_SECTOR,valores)
            registros = cursor.fetchall()
            dispositivos = []
            for registro in registros:
                dispositivo = Dispositivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                dispositivos.append(dispositivo)
                print(registro)
            return dispositivos
    
    @classmethod
    def seleccionarByUsuario(cls,usuario):
        with CursorPool() as cursor:
            valores = (usuario,)
            cursor.execute(cls._SELELCT_BY_USUARIO,valores)
            registros = cursor.fetchall()
            dispositivos = []
            for registro in registros:
                dispositivo = Dispositivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                dispositivos.append(dispositivo)
                print(registro)
            return dispositivos
    
    @classmethod
    def eliminar(cls, dispositivo):
        with CursorPool() as cursor:
            valores = (dispositivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar dispositivo, {dispositivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,dispositivo):
        with CursorPool() as cursor:
            valores = (dispositivo.disNombre, dispositivo.disTipo, dispositivo.disModelo,dispositivo.disSectores,dispositivo.disEstado )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar dispositivo, {dispositivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, dispositivo):
        with CursorPool() as cursor:
            valores = (dispositivo.disNombre, dispositivo.disTipo, dispositivo.disModelo,dispositivo.disSectores,dispositivo.disEstado,dispositivo.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar dispositivo, {dispositivo}')
            return cursor.rowcount

