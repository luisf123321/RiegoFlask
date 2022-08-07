

from re import T


class LoteMuestra:
    def __init__(self,id=None, arena=None, limo=None, arcilla=None,lote=None,tipoSuelo=None) -> None:
        self._id = id
        self._arena = arena
        self._limo = limo
        self._arcilla = arcilla
        self._lote = lote
        self._tipoSuelo = tipoSuelo
    
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
    def lote(self):
        return self._lote
    
    @lote.setter
    def lote(self, lote):
        self._lote = lote
    
    @property
    def tipoSuelo(self):
        return self._tipoSuelo
    
    @tipoSuelo.setter
    def tipoSuelo(self, tipoSuelo):
        self._tipoSuelo = tipoSuelo
    
    def __str__(self) -> str:
        return f'''
            Id muestra: {self._id}, arena: {self._arena} , limo: {self._limo},
            arcilla: {self._arcilla}, lote: {self._lote}, tipoSuelo : {self._tipoSuelo}
        '''