

class TipoCultivo:
    def __init__(self,id, nombre, variedad, referencia) -> None:
        self._id = id
        self._nombre = nombre
        self._variedad = variedad
        self._referencia  = referencia

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
    def variedad(self):
        return self._variedad
    
    @variedad.setter
    def variedad(self,variedad):
        self._variedad = variedad
    
    @property
    def referencia(self):
        return self._referencia
    
    @referencia
    def variedad(self, referencia):
        self._referencia = referencia
    
    def __str__(self) -> str:
        return f'''
            Id tipo cultivo: {self._id}, nombre: {self._nombre} , variedad : {self._variedad},
            referencia: {self._referencia}
        '''