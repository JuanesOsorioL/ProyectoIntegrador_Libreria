class LibroAutorDTO:
    libro_id: int = None
    autor_id: int = None
    antes_libro_id: int = None
    antes_autor_id: int = None

    def __init__(self, libro_id: int = None, autor_id: int = None,
                 antes_libro_id: int = None, antes_autor_id: int = None):
        self.libro_id = libro_id
        self.autor_id = autor_id
        self.antes_libro_id = antes_libro_id
        self.antes_autor_id = antes_autor_id

    # Getters
    def GetLibroId(self) -> int:
        return self.libro_id

    def GetAutorId(self) -> int:
        return self.autor_id

    def GetAntesLibroId(self) -> int:
        return self.antes_libro_id

    def GetAntesAutorId(self) -> int:
        return self.antes_autor_id

    # Setters
    def SetLibroId(self, value: int) -> None:
        self.libro_id = value

    def SetAutorId(self, value: int) -> None:
        self.autor_id = value

    def SetAntesLibroId(self, value: int) -> None:
        self.antes_libro_id = value

    def SetAntesAutorId(self, value: int) -> None:
        self.antes_autor_id = value

    # Representación en cadena
    def __str__(self) -> str:
        return (f"LibroID='{self.libro_id}', AutorID='{self.autor_id}', "
                f"AntesLibroID='{self.antes_libro_id}', AntesAutorID='{self.antes_autor_id}'")

    # Conversión simple a diccionario
    def to_dict_simple(self):
        return {
            "LibroId": self.libro_id,
            "AutorId": self.autor_id,
            "AntesLibroId": self.antes_libro_id,
            "AntesAutorId": self.antes_autor_id
        }