from Dtos.UsuarioDTO import UsuarioDTO

class UsuarioSistemaDTO:
    def __init__(self, id=None, usuario_id=None, nombre_usuario=None, contrasena=None,usuarioDTO: UsuarioDTO = None):
        self.id = id
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.usuarioDTO = usuarioDTO

    def get_id(self):
        return self.id

    def get_usuario_id(self):
        return self.usuario_id

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_contrasena(self):
        return self.contrasena

    def set_id(self, value):
        self.id = value

    def set_usuario_id(self, value):
        self.usuario_id = value

    def set_nombre_usuario(self, value):
        self.nombre_usuario = value

    def set_contrasena(self, value):
        self.contrasena = value

    def set_usuarioDTO(self, value:UsuarioDTO):
        self.usuarioDTO = value

    def get_usuarioDTO(self) -> UsuarioDTO:
        return self.usuarioDTO

    def to_dict(self):
        return {
            "id":  self.get_id(),
            "usuarioID": self.get_usuario_id(),
            "nombreUsuario": self.get_nombre_usuario(),
            "usuarioDTO": self.get_usuarioDTO().to_dict()
        }# "contrasena": self.get_contrasena(),