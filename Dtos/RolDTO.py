class RolDTO:

    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def GetId(self):
        return self.id

    def GetNombre(self):
        return self.nombre

    def SetId(self, value):
        self.id = value

    def SetNombre(self, value):
        self.nombre = value

    def to_dict(self):
        return {
            "id": self.GetId(),
            "nombre": self.GetNombre()
        }