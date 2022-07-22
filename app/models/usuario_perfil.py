

class UsuarioPerfil:
    def __init__(self, id, usuario, perfil) -> None:
        self._id = id
        self._usuario = usuario
        self._perfil = perfil
    
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
    def perfil(self):
        return self._perfil
    
    @perfil.setter
    def perfil(self, perfil):
        self._perfil = perfil

    def __str__(self) -> str:
        return f'''
            Id usuario perfil : {self._id}, usuario: {self._usuario} , perfil : {self._perfil}           
        '''
    