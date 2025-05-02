class UsuarioSistemaDTO:
    def __init__(self, id=None, usuario_id=None, username_payload=None, contrasena=None,rol_id=None):
        self.id = id
        self.usuario_id = usuario_id
        self.username_payload = username_payload
        self.contrasena = contrasena
        self.rol_id=rol_id

    def get_id(self):
        return self.id

    def get_usuario_id(self):
        return self.usuario_id

    def get_username_payload(self):
        return self.username_payload

    def get_contrasena(self):
        return self.contrasena

    def set_id(self, value):
        self.id = value

    def set_usuario_id(self, value):
        self.usuario_id = value

    def set_username_payload(self, value):
        self.username_payload = value

    def set_contrasena(self, value):
        self.contrasena = value
    
    def Get_RolId(self):
        return self.rol_id

    def Set_RolId(self, rol_id):
        self.rol_id = rol_id


        
    def __str__(self):
        return f"ID = {self.id} - UsuarioID = {self.usuario_id} - username_payload = {self.username_payload} - Contraseña = {self.contrasena}- Rol = {self.rol_id} "