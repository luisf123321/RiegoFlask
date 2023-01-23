

class Notificaciones:
    def __init__(self, id=None, usuario=None, mensaje=None,
                 estado=None, fechaOrigen=None,
                 fechaVista=None, titulo=None) -> None:
        self._id = id
        self._usuario = usuario
        self._mensaje = mensaje
        self._estado = estado
        self._fechaOrigen = fechaOrigen
        self._fechaVista = fechaVista
        self._titulo = titulo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def mensaje(self):
        return self._mensaje

    @mensaje.setter
    def mensaje(self, mensaje):
        self._mensaje = mensaje

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def fechaOrigen(self):
        return self._fechaOrigen

    @fechaOrigen.setter
    def fechaOrigen(self, fechaOrigen):
        self._fechaOrigen = fechaOrigen

    @property
    def fechaVista(self):
        return self._fechaVista

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @fechaVista.setter
    def fechaVista(self, fechaVista):
        self._fechaVista = fechaVista
