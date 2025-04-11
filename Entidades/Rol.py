class Rol:
    id: int = None
    nombre: str = None

    def GetId(self) -> int:
        return self.id;

    def SetId(self, value: int) -> None:
        self.id = value;

    def GetNombre(self) -> str:
        return self.nombre;

    def SetNombre(self, value: str) -> None:
        self.nombre = value;