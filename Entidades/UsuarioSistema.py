class UsuarioSistema:

    def __init__(self, id=None, usuario_id=None, username_payload=None,username_hmac=None, contrasena=None, rol_id=None, salt=None):
        self.id = id
        self.usuario_id = usuario_id
        self.username_payload = username_payload
        self.username_hmac=username_hmac
        self.contrasena = contrasena
        self.rol_id=rol_id
        self.salt=salt

    def Get_Id(self): 
        return self.id
    
    def Set_Id(self, id): 
        self.id = id

    def Get_UsuarioId(self): 
        return self.usuario_id
    
    def Set_UsuarioId(self, usuario_id): 
        self.usuario_id = usuario_id

    def Get_Username_Payload(self): 
        return self.username_payload
    
    def Set_Username_Payload(self, username_payload): 
        self.username_payload = username_payload

    def Get_Contrasena(self): 
        return self.contrasena
    
    def Set_Contrasena(self, contrasena): 
        self.contrasena = contrasena

    def get_Salt(self):
        return self.salt
    
    def set_Salt(self, value):
        self.salt = value
    
    def Get_Username_HMAC(self):
        return self.username_hmac

    def Set_Username_HMAC(self, username_hmac):
        self.username_hmac = username_hmac

    def Get_RolId(self):
        return self.rol_id

    def Set_RolId(self, rol_id):
        self.rol_id = rol_id