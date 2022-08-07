from app.utilites.cursor_pool import CursorPool
from app.models.admin_riego import AdminRiego
from app.utilites.logger_base import log
import json


class AdminRiegoDao:


    _SELELCT = 'SELECT * FROM admin_riego ORDER BY id'    
    _INSERT = 'INSERT INTO admin_riego (admin_tipo_riego, admin_nad, admin_efectividad, admin_caudal, admin_distancia, admin_radio) VALUES (%(int)s,%(float)s,%(float)s,%(float)s,%(float)s,%(float)s)'
    _UPDATE = 'UPDATE admin_riego SET  admin_tipo_riego=%s, admin_nad=%s, admin_efectividad=%s, admin_caudal=%s, admin_distancia=%s, admin_radio=%s WHERE id=%s'
    _DELETE = 'DELETE FROM admin_riego WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            adminRiegos = []
            for registro in registros:
                adminRiego = AdminRiego(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                adminRiegos.append(adminRiego)
                print(registro)
            return adminRiegos
    
    
    
    @classmethod
    def eliminar(cls, adminRiego):
        with CursorPool() as cursor:
            valores = (adminRiego.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar adminRiego, {adminRiego}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,adminRiego):
        with CursorPool() as cursor:
            valores = (adminRiego.tipoRiego, adminRiego.nad,adminRiego.efectividad,adminRiego.caudal,adminRiego.distancia, adminRiego.radio )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar adminRiego, {adminRiego}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, adminRiego):
        with CursorPool() as cursor:
            valores = (adminRiego.tipoRiego, adminRiego.nad,adminRiego.efectividad,adminRiego.caudal,adminRiego.distancia, adminRiego.radio )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar adminRiego, {adminRiego}')
            return cursor.rowcount