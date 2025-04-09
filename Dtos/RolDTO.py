class RolDTO:
    id: int = None
    Descripcion: str = None

    def GetId(self) -> int:
        return self.id;

    def SetId(self, value: int) -> None:
        self.id = value;

    def GetDescripcion(self) -> str:
        return self.Descripcion;

    def SetDescripcion(self, value: str) -> None:
        self.Descripcion = value;