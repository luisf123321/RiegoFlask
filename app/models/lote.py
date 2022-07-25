

class Lote:
    def __init__(self,id=None, nombre=None, finca=None, area=None, latitud=None, longitud=None, altitud=None) -> None:
        self._id = id
        self._nombre = nombre
        self._finca = finca
        self._area = area
        self._latidud = latitud
        self._longitud = longitud
        self._altitud = altitud
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    
    @property
    def latitud(self):
        return self._latidud
    
    @latitud.setter
    def latitud(self, latitud):
        self._latidud = latitud
    
    @property
    def longitud(self):
        return self._longitud
    
    @longitud.setter
    def longitud(self, longitud):
        self._longitud = longitud

    @property
    def altitud(self):
        return self._altitud
    
    @altitud.setter
    def altitud(self,altitud):
        self._altitud = altitud

    @property
    def finca(self):
        return self._finca
    
    @finca.setter
    def finca(self,finca):
        self._finca = finca
    
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self,area):
        self._area = area

    def __str__(self) -> str:
        return f'''
            Id lote: {self._id}, nombre: {self._nombre} , finca : {self._finca},
            altitud: {self._altitud}, longitud: {self._longitud}, latitud: {self._latidud}, area: {self._area}
        '''