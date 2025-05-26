from Entidades.Devolucion import Devolucion
from Dtos.DevolucionDTO import DevolucionDTO

def devolucion_a_dto(dev: Devolucion) -> DevolucionDTO:
    return DevolucionDTO(
        id=dev.id,
        prestamo_id=dev.prestamo_id,
        fecha_real_devolucion=dev.fecha_real_devolucion,
        estado_libro=dev.estado_libro,
        observaciones=dev.observaciones
    )

def dto_a_devolucion(dto: DevolucionDTO) -> Devolucion:
    return Devolucion(
        id=dto.id,
        prestamo_id=dto.prestamo_id,
        fecha_real_devolucion=dto.fecha_real_devolucion,
        estado_libro=dto.estado_libro,
        observaciones=dto.observaciones
    )

def fila_a_devolucion(fila: tuple) -> Devolucion:
    return Devolucion(
        id=fila[0],
        prestamo_id=fila[1],
        fecha_real_devolucion=fila[2],
        estado_libro=fila[3],
        observaciones=fila[4]
    )