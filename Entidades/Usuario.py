from Entidades.Rol import Rol

class Usuario:
    
    def __init__(
        self,
        id=None,
        nombre: bytes = None,
        nombre_hmac: str = None,
        email: bytes = None,
        email_hmac: str = None,
        telefono: bytes = None,
        telefono_hmac: str = None,
        direccion: bytes = None,
        direccion_hmac: str = None,
        fechaRegistro=None,
        rolId=None,
        rol: Rol = None
    ):
        self.id = id
        self.nombre = nombre
        self.nombre_hmac = nombre_hmac
        self.email = email
        self.email_hmac = email_hmac
        self.telefono = telefono
        self.telefono_hmac = telefono_hmac
        self.direccion = direccion
        self.direccion_hmac = direccion_hmac
        self.fechaRegistro = fechaRegistro
        self.rolId = rolId
        self.rol = rol

    def Get_Id(self):
        return self.id

    def Get_Nombre(self):
        return self.nombre

    def Get_NombreHmac(self):
        return self.nombre_hmac

    def Get_Email(self):
        return self.email

    def Get_EmailHmac(self):
        return self.email_hmac

    def Get_Telefono(self):
        return self.telefono

    def Get_TelefonoHmac(self):
        return self.telefono_hmac

    def Get_Direccion(self):
        return self.direccion

    def Get_DireccionHmac(self):
        return self.direccion_hmac

    def Get_FechaRegistro(self):
        return self.fechaRegistro

    def Get_RolId(self):
        return self.rolId

    def Get_Rol(self):
        return self.rol

    def Set_Id(self, value):
        self.id = value

    def Set_Nombre(self, value: bytes):
        self.nombre = value

    def Set_NombreHmac(self, value: str):
        self.nombre_hmac = value

    def Set_Email(self, value: bytes):
        self.email = value

    def Set_EmailHmac(self, value: str):
        self.email_hmac = value

    def Set_Telefono(self, value: bytes):
        self.telefono = value

    def Set_TelefonoHmac(self, value: str):
        self.telefono_hmac = value

    def Set_Direccion(self, value: bytes):
        self.direccion = value

    def Set_DireccionHmac(self, value: str):
        self.direccion_hmac = value

    def Set_FechaRegistro(self, value):
        self.fechaRegistro = value

    def Set_RolId(self, value):
        self.rolId = value

    def Set_Rol(self, rol: Rol):
        self.rol = rol