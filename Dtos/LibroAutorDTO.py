class LibroAutorDTO:
    libro_id: int = None
    autor_id: int = None

    def __init__(self, libro_id: int = None, autor_id: int = None):
        self.libro_id = libro_id
        self.autor_id = autor_id

    def GetLibroId(self) -> int:
        return self.libro_id

    def SetLibroId(self, value: int) -> None:
        self.libro_id = value

    def GetAutorId(self) -> int:
        return self.autor_id

    def SetAutorId(self, value: int) -> None:
        self.autor_id = value

    def __str__(self) -> str:
        return f"LibroID='{self.libro_id}', AutorID='{self.autor_id}'"