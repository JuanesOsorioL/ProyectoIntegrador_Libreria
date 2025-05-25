from Servicio.DevolucionServicio import DevolucionServicio
from Dtos.DevolucionDTO import DevolucionDTO
from Dtos.Generico.Respuesta import Respuesta

devolucionServicio = DevolucionServicio()

class DevolucionControlador:

    def insertarDevolucion(self, fecha: str, estado: str, observaciones: str) -> Respuesta:
        dto = DevolucionDTO(fecha_real_devolucion=fecha, estado_libro=estado, observaciones=observaciones)
        return devolucionServicio.insertarDevolucion(dto)

    def mostrarTodasLasDevoluciones(self) -> Respuesta:
        return devolucionServicio.MostrarTodasLasDevoluciones()

    def mostrarDevolucionPorId(self, id: int) -> Respuesta:
        dto = DevolucionDTO(id=id)
        return devolucionServicio.MostrarDevolucionPorId(dto)

    def actualizarDevolucion(self, id: int, fecha: str, estado: str, observaciones: str) -> Respuesta:
        dto = DevolucionDTO(id=id, fecha_real_devolucion=fecha, estado_libro=estado, observaciones=observaciones)
        return devolucionServicio.actualizarDevolucion(dto)

    def borrarDevolucion(self, id: int) -> Respuesta:
        dto = DevolucionDTO(id=id)
        return devolucionServicio.borrarDevolucion(dto)
