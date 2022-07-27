
class User:
    def __init__(self,id=None,nombre=None,apellido=None,documento=None, celular=None, direccion=None,user=None,password=None,correo=None ,tipoIdentificacion=None) -> None:
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._documento = documento 
        self._celular = celular
        self._direccion = direccion
        self._user = user
        self._password = password
        self._correo = correo
        self._tipoIdentificacion = tipoIdentificacion
    
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
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, documento):
        self._documento = documento
    
    @property
    def celular(self):
        return self._celular
    
    @celular.setter
    def celular(self, celular):
        self._celular = celular
    
    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion
    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, correo):
        self._correo = correo
    
    @property
    def tipoIdentificacion(self):
        return self._tipoIdentificacion
    
    @tipoIdentificacion.setter
    def tipoIdentificacion(self,tipoIdentificacion):
        self._tipoIdentificacion = tipoIdentificacion
    
    def __str__(self) -> str:
        return f'''
            Id usaurio: {self._id}, nombre: {self._nombre} , apellido : {self._apellido} , documento : {self._documento}
            celular: {self._celular}, correo: {self._correo}, user: {self._user}, password: {self._password} 
        '''

