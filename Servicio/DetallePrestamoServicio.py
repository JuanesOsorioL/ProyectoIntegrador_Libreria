from Dtos.DetallePrestamoDTO import DetallePrestamoDTO
from Repositorios.DetallePrestamoRepositorio import DetallePrestamoRepositorio
from Mapeadores.DetallePrestamoMapeadores import (
    detalle_prestamo_a_dto,
    dto_a_detalle_prestamo,
    fila_a_detalle_prestamo
)
from Dtos.Generico.Respuesta import Respuesta

class DetallePrestamoServicio:

    def __init__(self):
        self.repositorio = DetallePrestamoRepositorio()

    def insertarDetalle(self, dto: DetallePrestamoDTO) -> Respuesta:
        detalle = dto_a_detalle_prestamo(dto)
        codigo = self.repositorio.insertarDetalle(detalle)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(detalle.prestamo_id, detalle.libro_id)
            nuevo = fila_a_detalle_prestamo(fila)
            return Respuesta("Operación Exitosa", "Detalle registrado", detalle_prestamo_a_dto(nuevo).to_dict_simple())
        return Respuesta("Fallido", "No se pudo insertar", [])

    def mostrarTodos(self) -> Respuesta:
        filas = self.repositorio.mostrarTodos()
        return Respuesta("Operación Exitosa", "Listado de detalles", [detalle_prestamo_a_dto(fila_a_detalle_prestamo(f)).to_dict_simple() for f in filas])

    def mostrarPorId(self, dto: DetallePrestamoDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.prestamo_id, dto.libro_id)
        if fila:
            return Respuesta("Operación Exitosa", "Detalle encontrado", detalle_prestamo_a_dto(fila_a_detalle_prestamo(fila)).to_dict_simple())
        return Respuesta("Fallido", "No se encontró detalle", [])

    def mostrarPorPrestamo(self, prestamo_id: int) -> Respuesta:
        filas = self.repositorio.mostrarPorPrestamo(prestamo_id)
        return Respuesta("Operación Exitosa", f"Detalles del préstamo {prestamo_id}", [detalle_prestamo_a_dto(fila_a_detalle_prestamo(f)).to_dict_simple() for f in filas])

    def actualizarDetalle(self, dto: DetallePrestamoDTO) -> Respuesta:
        detalle = dto_a_detalle_prestamo(dto)
        codigo = self.repositorio.actualizarDetalle(detalle)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(dto.prestamo_id, dto.libro_id)
            actualizado = fila_a_detalle_prestamo(fila)
            return Respuesta("Operación Exitosa", "Detalle actualizado", detalle_prestamo_a_dto(actualizado).to_dict_simple())
        return Respuesta("Fallido", "No se pudo actualizar", [])

    def borrarDetalle(self, dto: DetallePrestamoDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.prestamo_id, dto.libro_id)
        if not fila:
            return Respuesta("Fallido", "Detalle no existe", [])
        codigo = self.repositorio.borrarDetalle(dto.prestamo_id, dto.libro_id)
        if codigo == 1:
            return Respuesta("Operación Exitosa", "Detalle eliminado", detalle_prestamo_a_dto(fila_a_detalle_prestamo(fila)).to_dict_simple())
        return Respuesta("Fallido", "No se pudo eliminar", [])
