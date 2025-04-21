class UsuarioSistema:
    def __init__(self, id=None, usuario_id=None, username=None, password_hash=None):
        self.id = id
        self.usuario_id = usuario_id
        self.username = username
        self.password_hash = password_hash

    def Get_Id(self): 
        return self.id
    
    def Set_Id(self, id): 
        self.id = id

    def Get_UsuarioId(self): 
        return self.usuario_id
    
    def Set_UsuarioId(self, usuario_id): 
        self.usuario_id = usuario_id

    def Get_Username(self): 
        return self.username
    
    def Set_Username(self, username): 
        self.username = username

    def Get_PasswordHash(self): 
        return self.password_hash
    
    def Set_PasswordHash(self, password_hash): 
        self.password_hash = password_hash