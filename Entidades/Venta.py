class Venta:
    def __init__(self, id=None, usuario_id=None, empleado_id=None, fecha=None, total=0.0):
        self.id = id
        self.usuario_id = usuario_id
        self.empleado_id = empleado_id
        self.fecha = fecha
        self.total = total