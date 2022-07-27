

class Cultivo:
    def __init__(self,id,cultivoNombre,cultivoLote,tipoCultivo,fechaInicio,fechaFinal, cultivoEstado) -> None:
        self._id = id
        self._cultivoNombre = cultivoNombre
        self._cultivoLote = cultivoLote
        self._tipoCultivo = tipoCultivo
        self._fechaInicio = fechaInicio
        self._fechaFinal = fechaFinal
        self._cultivoEstado = cultivoEstado

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id
    
    @property
    def cultivoNombre(self):
        return self._cultivoNombre
    
    @cultivoNombre.setter
    def cultivoNombre(self,cultivoNombre):
        self._cultivoNombre = cultivoNombre
    
    @property
    def cultivoLote(self):
        return self._cultivoLote
    
    @cultivoLote.setter
    def cultivoLote(self,cultivoLote):
        self._cultivoLote = cultivoLote
    
    @property
    def tipoCultivo(self):
        return self._tipoCultivo

    @tipoCultivo.setter
    def tipoCultivo(self,tipoCultivo):
        self._tipoCultivo = tipoCultivo
    
    @property
    def fechaInicio(self):
        return self._fechaInicio
    
    @fechaInicio.setter
    def fechaInicio(self,fechaInicio):
        self._fechaInicio = fechaInicio
    
    @property
    def fechaFinal(self):
        return self._fechaFinal

    @fechaFinal.setter
    def fechaFinal(self,fechaFinal):
        self._fechaFinal = fechaFinal

    @property
    def cultivoEstado(self):
        return self._cultivoEstado
    
    @cultivoEstado.setter
    def cultivoEstado(self,estado):
        self._cultivoEstado = estado
    
    def __str__(self) -> str:
        return f'''
            Id cultivo: {self._id}, Nombre cultivo: {self._cultivoNombre} , lote: {self._cultivoLote},
            tipo cultivo: {self._tipoCultivo}, Fecha inicio: {self._fechaInicio}, fecha final: {self._fechaFinal}, Estado : {self._cultivoEstado}
        '''