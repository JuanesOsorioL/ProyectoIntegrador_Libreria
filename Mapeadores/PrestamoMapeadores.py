from Entidades.Prestamo import Prestamo
from Dtos.PrestamoDTO import PrestamoDTO


def prestamo_a_dto(entidad: Prestamo) -> PrestamoDTO:
    return PrestamoDTO(
        id=entidad.id,
        usuario_id=entidad.usuario_id,
        empleado_id=entidad.empleado_id,
        fecha_prestamo=entidad.fecha_prestamo,
        fecha_devolucion=entidad.fecha_devolucion,
        estado=entidad.estado
    )

def dto_a_prestamo(dto: PrestamoDTO) -> Prestamo:
    return Prestamo(
        id=dto.id,
        usuario_id=dto.usuario_id,
        empleado_id=dto.empleado_id,
        fecha_prestamo=dto.fecha_prestamo,
        fecha_devolucion=dto.fecha_devolucion,
        estado=dto.estado
    )

def fila_a_prestamo(fila: tuple) -> Prestamo:
    return Prestamo(*fila)