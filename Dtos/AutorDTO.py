class AutorDTO:
    id: int = None
    nombre: str = None
    nacionalidad: str = None

    def __init__(self, id: int = None, nombre: str = "", nacionalidad: str = ""):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetNacionalidad(self) -> str:
        return self.nacionalidad

    def SetNacionalidad(self, value: str) -> None:
        self.nacionalidad = value

    def __str__(self) -> str:
        return f"Id='{self.id}', Nombre='{self.nombre}', Nacionalidad='{self.nacionalidad}'"
