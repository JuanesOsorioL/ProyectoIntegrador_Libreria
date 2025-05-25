from Servicio.DetallePrestamoServicio import DetallePrestamoServicio
from Dtos.DetallePrestamoDTO import DetallePrestamoDTO
from Dtos.Generico.Respuesta import Respuesta

class DetallePrestamoControlador:

    def __init__(self):
        self.servicio = DetallePrestamoServicio()

    def insertarDetalle(self, prestamo_id, libro_id, cantidad) -> Respuesta:
        dto = DetallePrestamoDTO(prestamo_id, libro_id, cantidad)
        return self.servicio.insertarDetalle(dto)

    def mostrarTodosLosDetalles(self) -> Respuesta:
        return self.servicio.mostrarTodos()

    def mostrarDetallePorId(self, prestamo_id, libro_id) -> Respuesta:
        dto = DetallePrestamoDTO(prestamo_id, libro_id)
        return self.servicio.mostrarPorId(dto)

    def mostrarDetallesDeUnPrestamo(self, prestamo_id: int) -> Respuesta:
        return self.servicio.mostrarPorPrestamo(prestamo_id)

    def actualizarDetalle(self, prestamo_id, libro_id, cantidad) -> Respuesta:
        dto = DetallePrestamoDTO(prestamo_id, libro_id, cantidad)
        return self.servicio.actualizarDetalle(dto)

    def borrarDetalle(self, prestamo_id, libro_id) -> Respuesta:
        dto = DetallePrestamoDTO(prestamo_id, libro_id)
        return self.servicio.borrarDetalle(dto)
