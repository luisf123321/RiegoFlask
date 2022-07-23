

from utilites.cursor_pool import CursorPool
from models.usuario import User
from utilites.logger_base import log

class UsuarioDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM usuario ORDER BY id'
    _INSERT = 'INSERT INTO usuario (usu_nombre, usu_apellido, usu_numero_identificacion, usu_celular, usu_direccion, usu_user, usu_password,usu_correo, usu_tipo_identificacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE usuario SET  usu_nombre=%s, usu_apellido=%s, usu_numero_identificacion=%s, usu_celular=%s, usu_direccion=%s, usu_user=%s, usu_password=%s, usu_correo=%s,usu_tipo_identificacion=%s WHERE id=%s'
    _DELETE = 'DELETE FROM usuario WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = User(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8], registro[9])
                usuarios.append(usuario)
                print(usuario)
            return usuarios
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar usuario, {usuario}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,usuario):
        with CursorPool() as cursor:
            valores = (usuario.nombre, usuario.apellido, usuario.documento,usuario.celular,usuario.direccion,usuario.user,usuario.password,usuario.correo,usuario.tipoIdentificacion )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar usuario, {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.nombre, usuario.apellido, usuario.documento,usuario.celular,usuario.direccion,usuario.user,usuario.password,usuario.correo,usuario.tipoIdentificacion,usuario.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar usuario, {usuario}')
            return cursor.rowcount