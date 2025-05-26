from Dtos.DetalleVentaDTO import DetalleVentaDTO
from Repositorios.DetalleVentaRepositorio import DetalleVentaRepositorio
from Mapeadores.Mapeadores import (
    detalle_venta_a_dto,
    dto_a_detalle_venta,
    fila_a_detalle_venta
)
from Dtos.Generico.Respuesta import Respuesta

class DetalleVentaServicio:

    def __init__(self):
        self.repositorio = DetalleVentaRepositorio()

    def insertarDetalle(self, dto: DetalleVentaDTO) -> Respuesta:
        detalle = dto_a_detalle_venta(dto)
        codigo = self.repositorio.insertarDetalle(detalle)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(detalle.venta_id, detalle.libro_id)
            nuevo = fila_a_detalle_venta(fila)
            return Respuesta("Operación Exitosa", "Detalle registrado", [str(detalle_venta_a_dto(nuevo))])
        else:
            return Respuesta("Fallido", "No se pudo insertar el detalle", [])

    def mostrarTodos(self) -> Respuesta:
        filas = self.repositorio.mostrarTodos()
        resultado = [str(detalle_venta_a_dto(fila_a_detalle_venta(f))) for f in filas]
        return Respuesta("Operación Exitosa", "Listado de detalles de venta", resultado)

    def mostrarPorId(self, dto: DetalleVentaDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.venta_id, dto.libro_id)
        if fila:
            detalle = fila_a_detalle_venta(fila)
            return Respuesta("Operación Exitosa", "Detalle encontrado", [str(detalle_venta_a_dto(detalle))])
        else:
            return Respuesta("Fallido", "Detalle no encontrado", [])

    def mostrarPorVenta(self, venta_id: int) -> Respuesta:
        filas = self.repositorio.mostrarPorVenta(venta_id)
        resultado = [str(detalle_venta_a_dto(fila_a_detalle_venta(f))) for f in filas]
        return Respuesta("Operación Exitosa", f"Detalles de la venta {venta_id}", resultado)

    def actualizarDetalle(self, dto: DetalleVentaDTO) -> Respuesta:
        detalle = dto_a_detalle_venta(dto)
        codigo = self.repositorio.actualizarDetalle(detalle)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(detalle.venta_id, detalle.libro_id)
            actualizado = fila_a_detalle_venta(fila)
            return Respuesta("Operación Exitosa", "Detalle actualizado", [str(detalle_venta_a_dto(actualizado))])
        else:
            return Respuesta("Fallido", "No se pudo actualizar el detalle", [])

    def borrarDetalle(self, dto: DetalleVentaDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.venta_id, dto.libro_id)
        if not fila:
            return Respuesta("Fallido", "Detalle no existe", [])
        codigo = self.repositorio.borrarDetalle(dto.venta_id, dto.libro_id)
        if codigo == 1:
            detalle = fila_a_detalle_venta(fila)
            return Respuesta("Operación Exitosa", "Detalle eliminado", [str(detalle_venta_a_dto(detalle))])
        else:
            return Respuesta("Fallido", "No se pudo eliminar", [])
    