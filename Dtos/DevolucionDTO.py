# DevolucionDTO.py
class DevolucionDTO:
    def __init__(self, id: int = None, fecha_real_devolucion: str = "", estado_libro: str = "", observaciones: str = ""):
        self.id = id
        self.fecha_real_devolucion = fecha_real_devolucion
        self.estado_libro = estado_libro
        self.observaciones = observaciones

    def __str__(self) -> str:
        return f"Id={self.id}, Fecha={self.fecha_real_devolucion}, Estado='{self.estado_libro}', Observaciones='{self.observaciones}'"
