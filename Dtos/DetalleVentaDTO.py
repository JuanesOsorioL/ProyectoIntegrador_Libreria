class DetalleVentaDTO:
    def __init__(self, venta_id=None, libro_id=None, cantidad=0, precio_unitario=0.0):
        self.venta_id = venta_id
        self.libro_id = libro_id
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)
        self.subtotal = self.cantidad * self.precio_unitario

    def __str__(self):
        return (f"Venta ID: {self.venta_id}, Libro ID: {self.libro_id}, "
                f"Cantidad: {self.cantidad}, Precio Unitario: {self.precio_unitario}, "
                f"Subtotal: {self.subtotal}")
    
    def to_dict_simple(self):
        return {
            "VentaId": self.venta_id,
            "LibroId": self.libro_id,
            "Cantidad": self.cantidad,
            "PrecioUnitario": self.precio_unitario,
            "Subtotal": self.subtotal
        }