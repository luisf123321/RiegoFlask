from .conexion import Conexion
from .logger_base import log

class CursorPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
    

    def __enter__(self):
        log.debug("inicio del metodo enter")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self,tipo_exc,exc_val, detalle_exc):
        log.debug(f'ejecuta metodo exit')
        if exc_val:
            self._conexion.rollback()
            log.error(f'error exc, {exc_val}')
        else:
            self._conexion.commit()
            log.debug(f'commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConecion(self._conexion)


if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug(f'bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())