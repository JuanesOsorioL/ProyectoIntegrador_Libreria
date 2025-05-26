# DevolucionDTO.py
class DevolucionDTO:
    def __init__(self, id = None,prestamo_id=None, fecha_real_devolucion= None, estado_libro= None, observaciones= None):
        self.id = id
        self.prestamo_id = prestamo_id
        self.fecha_real_devolucion = fecha_real_devolucion
        self.estado_libro = estado_libro
        self.observaciones = observaciones

    def __str__(self) -> str:
        return f"Id={self.id}, Fecha={self.fecha_real_devolucion}, Estado='{self.estado_libro}', Observaciones='{self.observaciones}'"
    
    def to_dict_simple(self):
        return {
            "id":             self.id,
            "prestamo id":    self.prestamo_id,
            "Fecha":         self.fecha_real_devolucion,
            "Estado":         self.estado_libro,
            "Observaciones":         self.observaciones
        }
