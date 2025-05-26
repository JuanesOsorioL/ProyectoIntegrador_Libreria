from Entidades.DetallePrestamo import DetallePrestamo
from Dtos.DetallePrestamoDTO import DetallePrestamoDTO

def detalle_prestamo_a_dto(entidad: DetallePrestamo) -> DetallePrestamoDTO:
    return DetallePrestamoDTO(
        prestamo_id=entidad.prestamo_id,
        libro_id=entidad.libro_id,
        cantidad=entidad.cantidad
    )

def dto_a_detalle_prestamo(dto: DetallePrestamoDTO) -> DetallePrestamo:
    return DetallePrestamo(
        prestamo_id=dto.prestamo_id,
        libro_id=dto.libro_id,
        cantidad=dto.cantidad
    )

def fila_a_detalle_prestamo(fila: tuple) -> DetallePrestamo:
    return DetallePrestamo(
        prestamo_id=fila[0],
        libro_id=fila[1],
        cantidad=fila[2]
    )