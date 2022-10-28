

from re import T


class MuestraSuelo:
    def __init__(self,id=None, arena=None, limo=None, arcilla=None,tipoSuelo=None, usuario=None, fecha=None) -> None:
        self._id = id
        self._arena = arena
        self._limo = limo
        self._arcilla = arcilla
        self._tipoSuelo = tipoSuelo
        self._usuario = usuario
        self._fecha = fecha
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, arena):
        self._arena = arena
    
    @property
    def limo(self):
        return self._limo
    
    @limo.setter
    def limo(self, limo):
        self._limo = limo
    
    @property
    def arcilla(self):
        return self._arcilla

    @arcilla.setter
    def arcilla(self, arcilla):
        self._arcilla = arcilla
    
    
    @property
    def tipoSuelo(self):
        return self._tipoSuelo
    
    @tipoSuelo.setter
    def tipoSuelo(self, tipoSuelo):
        self._tipoSuelo = tipoSuelo
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario
    
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
    
    def __str__(self) -> str:
        return f'''
            Id muestra: {self._id}, arena: {self._arena} , limo: {self._limo},
            arcilla: {self._arcilla},  tipoSuelo : {self._tipoSuelo}
        '''