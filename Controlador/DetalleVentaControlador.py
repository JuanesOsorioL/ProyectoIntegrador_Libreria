from Servicio.DetalleVentaServicio import DetalleVentaServicio
from Dtos.DetalleVentaDTO import DetalleVentaDTO
from Dtos.Generico.Respuesta import Respuesta

class DetalleVentaControlador:

    def __init__(self):
        self.servicio = DetalleVentaServicio()

    def insertarDetalle(self, venta_id, libro_id, cantidad, precio_unitario) -> Respuesta:
        dto = DetalleVentaDTO(venta_id=venta_id, libro_id=libro_id, cantidad=cantidad, precio_unitario=precio_unitario)
        return self.servicio.insertarDetalle(dto)

    def mostrarTodosLosDetalles(self) -> Respuesta:
        return self.servicio.mostrarTodos()

    def mostrarDetallePorId(self, venta_id, libro_id) -> Respuesta:
        dto = DetalleVentaDTO(venta_id=venta_id, libro_id=libro_id)
        return self.servicio.mostrarPorId(dto)

    def mostrarDetallesDeUnaVenta(self, venta_id: int) -> Respuesta:
        return self.servicio.mostrarPorVenta(venta_id)

    def actualizarDetalle(self, venta_id, libro_id, cantidad, precio_unitario) -> Respuesta:
        dto = DetalleVentaDTO(venta_id=venta_id, libro_id=libro_id, cantidad=cantidad, precio_unitario=precio_unitario)
        return self.servicio.actualizarDetalle(dto)

    def borrarDetalle(self, venta_id, libro_id) -> Respuesta:
        dto = DetalleVentaDTO(venta_id=venta_id, libro_id=libro_id)
        return self.servicio.borrarDetalle(dto)