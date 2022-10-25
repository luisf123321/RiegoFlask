

from utilites.cursor_pool import CursorPool
from models.usuario_perfil import UsuarioPerfil
from utilites.logger_base import log

class UsuarioPerfilDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM usuario_perfil ORDER BY id'
    _INSERT = 'INSERT INTO usuario_perfil (usu_per_idusuario, usu_per_idperfil) VALUES (%s,%s)'
    _UPDATE = 'UPDATE usuario_perfil SET  usu_per_idusuario=%s, usu_per_idperfil=%s WHERE id=%s'
    _DELETE = 'DELETE FROM usuario_perfil WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            usuarioPerfiles = []
            for registro in registros:
                usuarioPerfil = UsuarioPerfil(registro[0], registro[1], registro[2])
                usuarioPerfiles.append(usuarioPerfil)
                print(usuarioPerfil)
            return usuarioPerfiles
    
    
    
    

    