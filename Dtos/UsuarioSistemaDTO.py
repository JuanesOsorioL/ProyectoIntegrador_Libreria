class UsuarioSistemaDTO:
    def __init__(self, id=None, usuario_id=None, nombre_usuario=None, contrasena=None, rolId=None):
        self.id = id
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rolId = rolId


    def get_id(self):
        return self.id

    def get_usuario_id(self):
        return self.usuario_id

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_contrasena(self):
        return self.contrasena
    
    def get_rol_id(self):
        return self.rolId
    
    def set_rol_id(self, value):
        self.rolId = value

    def set_id(self, value):
        self.id = value

    def set_usuario_id(self, value):
        self.usuario_id = value

    def set_nombre_usuario(self, value):
        self.nombre_usuario = value

    def set_contrasena(self, value):
        self.contrasena = value

    def __str__(self):
        return f"ID = {self.id} - UsuarioID = {self.usuario_id} - nombre_usuario = {self.nombre_usuario} - Contraseña = {self.contrasena}"