

class TipoDispositivo:
    def __init__(self, id, categoria, caracteristica) -> None:
        self._id = id
        self._categoria = categoria
        self._caracteristica = caracteristica
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,categoria):
        self._categoria = categoria
    
    @property
    def caracteristica(self):
        return self._caracteristica
    
    @caracteristica.setter
    def caracteristica(self,caracteristica):
        self._caracteristica = caracteristica
    
    def __str__(self) -> str:
        return f'''
            Id tipo dispositivo: {self._id}, categoria: {self._categoria} , caracteristicas : {self._caracteristica}
           
        '''