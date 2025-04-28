class EditorialDTO:
    id: int = None
    nombre: str = None
    pais: str = None

    def __init__(self, id: int = None, nombre: str = "", pais: str = ""):
     
        self.id = id
        self.nombre = nombre
        self.pais = pais

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetPais(self) -> str:
        return self.pais

    def SetPais(self, value: str) -> None:
        self.pais = value

    def __str__(self) -> str:
        return f"Id='{self.id}', Nombre='{self.nombre}', País='{self.pais}'"