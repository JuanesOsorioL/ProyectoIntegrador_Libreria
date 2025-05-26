class DetallePrestamoDTO:
    def __init__(self, prestamo_id=None, libro_id=None, cantidad=0):
        self.prestamo_id = prestamo_id
        self.libro_id = libro_id
        self.cantidad = cantidad

    def __str__(self):
        return f"Prestamo ID: {self.prestamo_id}, Libro ID: {self.libro_id}, Cantidad: {self.cantidad}"

    def to_dict_simple(self):
        return {
            "PrestamoId": self.prestamo_id,
            "LibroId": self.libro_id,
            "Cantidad": self.cantidad
        }