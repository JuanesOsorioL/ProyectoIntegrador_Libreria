class Rol:
    def __init__(self, id=None, nombre=None, nombre_hmac=None):
        self.id = id
        self.nombre = nombre
        self.nombre_hmac = nombre_hmac

    def GetId(self):
        return self.id

    def GetNombre(self):
        return self.nombre

    def GetNombreHmac(self):
        return self.nombre_hmac
    
    def SetId(self, value):
        self.id = value

    def SetNombre(self, value):
        self.nombre = value

    def SetNombreHmac(self, value):
        self.nombre_hmac = value