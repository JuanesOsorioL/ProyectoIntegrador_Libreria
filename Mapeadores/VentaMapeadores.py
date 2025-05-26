from Entidades.Venta import Venta
from Dtos.VentaDTO import VentaDTO

def venta_a_dto(venta: Venta) -> VentaDTO:
    return VentaDTO(venta.id,venta.usuario_id,venta.empleado_id,venta.fecha,venta.total)

def dto_a_venta(dto: VentaDTO) -> Venta:
    return Venta(dto.id,dto.usuario_id,dto.empleado_id,dto.fecha,dto.total)

def fila_a_venta(fila: tuple) -> Venta:
    return Venta(*fila)