# Devolucion.py
class Devolucion:
    def __init__(self, id = None, prestamo_id=None, fecha_real_devolucion = None, estado_libro = None, observaciones = None):
        self.id = id
        self.prestamo_id = prestamo_id
        self.fecha_real_devolucion = fecha_real_devolucion
        self.estado_libro = estado_libro
        self.observaciones = observaciones

    def GetPrestamoId(self) -> int:
        return self.prestamo_id

    def SetPrestamoId(self, value: int) -> None:
        self.prestamo_id = value

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
        
    def to_dict_simple(self):
        return {
            "id":             self.id,
            "prestamo":             self.prestamo_id,
            "Fecha":         self.fecha_real_devolucion,
            "Estado":         self.estado_libro,
            "Observaciones":         self.observaciones
        }