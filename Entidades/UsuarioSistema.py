class UsuarioSistema:

    def __init__(self, id=None, usuario_id=None, nombre_usuario=None,nombre_usuario_hmac=None, contrasena=None, salt=None):
        self.id = id
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.nombre_usuario_hmac=nombre_usuario_hmac
        self.contrasena = contrasena
        self.salt=salt

    def Get_Id(self): 
        return self.id
    
    def Set_Id(self, value): 
        self.id = value

    def Get_UsuarioId(self): 
        return self.usuario_id
    
    def Set_UsuarioId(self, value): 
        self.usuario_id = value

    def Get_nombre_usuario(self): 
        return self.nombre_usuario
    
    def Set_nombre_usuario(self, value): 
        self.nombre_usuario = value

    def Get_Contrasena(self): 
        return self.contrasena
    
    def Set_Contrasena(self, value): 
        self.contrasena = value

    def Get_Salt(self):
        return self.salt
    
    def Set_Salt(self, value):
        self.salt = value
    
    def Get_nombre_Usuario_HMAC(self):
        return self.nombre_usuario_hmac

    def Set_nombre_Usuario_HMAC(self, value):
        self.nombre_usuario_hmac = value