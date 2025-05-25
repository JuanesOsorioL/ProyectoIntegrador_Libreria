class LibroCategoriaDTO:
    libro_id: int = None
    categoria_id: int = None

    def __init__(self, libro_id: int = None, categoria_id: int = None):
        self.libro_id = libro_id
        self.categoria_id = categoria_id

    def GetLibroId(self) -> int:
        return self.libro_id

    def SetLibroId(self, value: int) -> None:
        self.libro_id = value

    def GetCategoriaId(self) -> int:
        return self.categoria_id

    def SetCategoriaId(self, value: int) -> None:
        self.categoria_id = value

    def __str__(self) -> str:
        return f"LibroId='{self.libro_id}', CategoriaId='{self.categoria_id}'"