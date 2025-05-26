class VentaDTO:
    def __init__(self, id=None, usuario_id=None, empleado_id=None, fecha=None, total=0.0):
        self.id = id
        self.usuario_id = usuario_id
        self.empleado_id = empleado_id
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return (f"ID: {self.id}, Usuario ID: {self.usuario_id}, Empleado ID: {self.empleado_id}, "
                f"Fecha: {self.fecha}, Total: {self.total}")
    
    def to_dict_simple(self):
        return {
            "Id": self.id,
            "UsuarioId": self.usuario_id,
            "EmpleadoId": self.empleado_id,
            "Fecha": self.fecha,
            "Total": self.total
        }