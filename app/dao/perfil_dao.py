from utilites.cursor_pool import CursorPool
from models.perfil import Perfil
from utilites.logger_base import log

class PerfilDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM perfil ORDER BY id'
    _INSERT = 'INSERT INTO perfil (per_nombre, per_descripcion) VALUES (%s,%s)'
    _UPDATE = 'UPDATE perfil SET  per_nombre=%s, per_descripcion=%s WHERE id=%s'
    _DELETE = 'DELETE FROM perfil WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            perfiles = []
            for registro in registros:
                perfil = Perfil(registro[0], registro[1], registro[2])
                perfiles.append(perfil)
                print(perfil)
            return perfiles