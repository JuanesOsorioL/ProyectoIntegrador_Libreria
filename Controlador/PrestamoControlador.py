from Servicio.PrestamoServicio import PrestamoServicio
from Dtos.PrestamoDTO import PrestamoDTO
from Dtos.Generico.Respuesta import Respuesta

class PrestamoControlador:

    def __init__(self):
        self.servicio = PrestamoServicio()

    def insertarPrestamo(self, cliente_id, empleado_id, fecha_prestamo, fecha_devolucion, estado) -> Respuesta:
        dto = PrestamoDTO(
            usuario_id=cliente_id,
            empleado_id=empleado_id,
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion=fecha_devolucion,
            estado=estado
        )
        return self.servicio.insertarPrestamo(dto)

    def mostrarTodosLosPrestamos(self) -> Respuesta:
        return self.servicio.mostrarTodos()

    def mostrarPrestamoPorId(self, id: int) -> Respuesta:
        dto = PrestamoDTO(id=id)
        return self.servicio.mostrarPorId(dto)

    def actualizarPrestamo(self, id: int, cliente_id, empleado_id, fecha_prestamo, fecha_devolucion, estado) -> Respuesta:
        dto = PrestamoDTO(
            id=id,
            usuario_id=cliente_id,
            empleado_id=empleado_id,
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion=fecha_devolucion,
            estado=estado
        )
        return self.servicio.actualizarPrestamo(dto)

    def borrarPrestamo(self, id: int) -> Respuesta:
        dto = PrestamoDTO(id=id)
        return self.servicio.borrarPrestamo(dto)
