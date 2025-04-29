class UsuarioSistemaDTO:
    def __init__(self, id=None, usuario_id=None, username=None, contrasena=None):
        self.id = id
        self.usuario_id = usuario_id
        self.username = username
        self.contrasena = contrasena

    def get_id(self):
        return self.id

    def get_usuario_id(self):
        return self.usuario_id

    def get_username(self):
        return self.username

    def get_contrasena(self):
        return self.contrasena

    def set_id(self, value):
        self.id = value

    def set_usuario_id(self, value):
        self.usuario_id = value

    def set_username(self, value):
        self.username = value

    def set_contrasena(self, value):
        self.contrasena = value
        
    def __str__(self):
        return f"ID = {self.id} - UsuarioID = {self.usuario_id} - UserName = {self.username} - Contraseña = {self.contrasena}"