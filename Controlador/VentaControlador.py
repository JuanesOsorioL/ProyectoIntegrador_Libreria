from Servicio.VentaServicio import VentaServicio
from Dtos.VentaDTO import VentaDTO
from Dtos.Generico.Respuesta import Respuesta

class VentaControlador:

    def __init__(self):
        self.servicio = VentaServicio()

    def insertarVenta(self, cliente_id, empleado_id, total) -> Respuesta:
        dto = VentaDTO(usuario_id=cliente_id, empleado_id=empleado_id, total=total)
        return self.servicio.insertarVenta(dto)

    def mostrarTodasLasVentas(self) -> Respuesta:
        return self.servicio.mostrarTodos()

    def mostrarVentaPorId(self, id: int) -> Respuesta:
        dto = VentaDTO(id=id)
        return self.servicio.mostrarPorId(dto)

    def actualizarVenta(self, id: int, cliente_id, empleado_id, fecha, total) -> Respuesta:
        dto = VentaDTO(id=id, usuario_id=cliente_id, empleado_id=empleado_id, fecha=fecha, total=total)
        return self.servicio.actualizarVenta(dto)

    def borrarVenta(self, id: int) -> Respuesta:
        dto = VentaDTO(id=id)
        return self.servicio.borrarVenta(dto)
