class DetalleVenta:
    def __init__(self, venta_id=None, libro_id=None, cantidad=0, precio_unitario=0.0):
        self.venta_id = venta_id
        self.libro_id = libro_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = self.cantidad * self.precio_unitario
