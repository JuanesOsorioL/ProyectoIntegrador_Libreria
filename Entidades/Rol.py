

class Rol:
	
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;

    Descripcion: str = None;

    def GetDescripcion(self) -> str:
        return self.Descripcion;
    def SetDescripcion(self, value: str) -> None:
        self.Descripcion = value;


    PuedePrestar: str = None;

    def GetNombre(self) -> str:
        return self.Nombre;
    def SetNombre(self, value: str) -> None:
        self.Nombre = value;

    PuedePrestar: bool = None;

    def GetPuedePrestar(self) -> bool:
        return self.PuedePrestar;
    def SetPuedePrestar(self, value: bool) -> None:
        self.PuedePrestar = value;


    PuedeReservar: bool = None;

    def GetPuedeReservar(self) -> bool:
        return self.PuedeReservar;
    def SetPuedeReservar(self, value: bool) -> None:
        self.PuedeReservar = value;


    MaxLibros: int = None;

    def GetMaxLibros(self) -> int:
        return self.MaxLibros;
    def SetMaxLibros(self, value: int) -> None:
        self.MaxLibros = value;