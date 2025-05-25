class Prestamo:
    def __init__(self, id=None, usuario_id=None, empleado_id=None,
                 fecha_prestamo=None, fecha_devolucion=None, estado=None):
        self.id = id
        self.usuario_id = usuario_id
        self.empleado_id = empleado_id
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
