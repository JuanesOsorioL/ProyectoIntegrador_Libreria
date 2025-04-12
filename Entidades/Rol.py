class Rol:
    id: int = None
    nombre: str = None

    def __init__(self, id: int = None, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def GetId(self) -> int:
        return self.id;

    def SetId(self, value: int) -> None:
        self.id = value;

    def GetNombre(self) -> str:
        return self.nombre;

    def SetNombre(self, value: str) -> None:
        self.nombre = value;