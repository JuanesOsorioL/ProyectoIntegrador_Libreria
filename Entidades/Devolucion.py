# Devolucion.py
class Devolucion:
    def __init__(self, id: int = None, fecha_real_devolucion: str = "", estado_libro: str = "", observaciones: str = ""):
        self.id = id
        self.fecha_real_devolucion = fecha_real_devolucion
        self.estado_libro = estado_libro
        self.observaciones = observaciones

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetFechaRealDevolucion(self) -> str:
        return self.fecha_real_devolucion

    def SetFechaRealDevolucion(self, value: str) -> None:
        self.fecha_real_devolucion = value

    def GetEstadoLibro(self) -> str:
        return self.estado_libro

    def SetEstadoLibro(self, value: str) -> None:
        self.estado_libro = value

    def GetObservaciones(self) -> str:
        return self.observaciones

    def SetObservaciones(self, value: str) -> None:
        self.observaciones = value
