from Entidades.DetalleVenta import DetalleVenta
from Dtos.DetalleVentaDTO import DetalleVentaDTO


def detalle_venta_a_dto(entidad: DetalleVenta) -> DetalleVentaDTO:
    return DetalleVentaDTO(
        venta_id=entidad.venta_id,
        libro_id=entidad.libro_id,
        cantidad=entidad.cantidad,
        precio_unitario=entidad.precio_unitario
    )

def dto_a_detalle_venta(dto: DetalleVentaDTO) -> DetalleVenta:
    return DetalleVenta(
        venta_id=dto.venta_id,
        libro_id=dto.libro_id,
        cantidad=dto.cantidad,
        precio_unitario=dto.precio_unitario
    )

def fila_a_detalle_venta(fila: tuple) -> DetalleVenta:
    return DetalleVenta(
        venta_id=fila[0],
        libro_id=fila[1],
        cantidad=fila[2],
        precio_unitario=float(fila[3])  # subtotal se recalcula automáticamente
    )