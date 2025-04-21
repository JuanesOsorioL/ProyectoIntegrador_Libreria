class UsuarioSistemaDTO:
    def __init__(self, id=None, usuario_id=None, username=None, password_hash=None):
        self.id = id
        self.usuario_id = usuario_id
        self.username = username
        self.password_hash = password_hash

    def __str__(self):
        return f"{self.id} - {self.usuario_id} - {self.username}"