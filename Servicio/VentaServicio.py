from Dtos.VentaDTO import VentaDTO
from Repositorios.VentaRepositorio import VentaRepositorio
from Mapeadores.Mapeadores import venta_a_dto, dto_a_venta, fila_a_venta
from Dtos.Generico.Respuesta import Respuesta

class VentaServicio:

    def __init__(self):
        self.repositorio = VentaRepositorio()

    def insertarVenta(self, dto: VentaDTO) -> Respuesta:
        venta = dto_a_venta(dto)
        nuevo_id, codigo = self.repositorio.insertarVenta(venta)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(nuevo_id)
            nueva_venta = fila_a_venta(fila)
            return Respuesta("Operación Exitosa", "Venta registrada", [str(venta_a_dto(nueva_venta))])
        else:
            return Respuesta("Fallido", "No se pudo insertar la venta", [])

    def mostrarTodos(self) -> Respuesta:
        filas = self.repositorio.mostrarTodos()
        resultado = [str(venta_a_dto(fila_a_venta(f))) for f in filas]
        return Respuesta("Operación Exitosa", "Listado de ventas", resultado)

    def mostrarPorId(self, dto: VentaDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.id)
        if fila:
            venta = fila_a_venta(fila)
            return Respuesta("Operación Exitosa", "Venta encontrada", [str(venta_a_dto(venta))])
        else:
            return Respuesta("Fallido", "Venta no encontrada", [])

    def actualizarVenta(self, dto: VentaDTO) -> Respuesta:
        venta = dto_a_venta(dto)
        codigo = self.repositorio.actualizarVenta(venta)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(venta.id)
            actualizada = fila_a_venta(fila)
            return Respuesta("Operación Exitosa", "Venta actualizada", [str(venta_a_dto(actualizada))])
        else:
            return Respuesta("Fallido", "No se pudo actualizar", [])

    def borrarVenta(self, dto: VentaDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.id)
        if not fila:
            return Respuesta("Fallido", "Venta no existe", [])
        codigo = self.repositorio.borrarVenta(dto.id)
        if codigo == 1:
            venta = fila_a_venta(fila)
            return Respuesta("Operación Exitosa", "Venta eliminada", [str(venta_a_dto(venta))])
        else:
            return Respuesta("Fallido", "No se pudo eliminar", [])
