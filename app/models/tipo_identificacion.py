
class TipoIdentificacion:
    def __init__(self, id,nombre,descripcion ) -> None:
        self._id = id
        self._nombre = nombre
        self._description = descripcion
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._description

    @descripcion.setter
    def descripcion(self, description):
        self._description = description

    def __str__(self) -> str:
        return f'''
            Id tipo identificacion: {self._id}, nombre: {self._nombre} , descripcion : {self._description}           
        '''