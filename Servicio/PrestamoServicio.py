from Dtos.PrestamoDTO import PrestamoDTO
from Entidades.Prestamo import Prestamo
from Repositorios.PrestamoRepositorio import PrestamoRepositorio
from Mapeadores.Mapeadores import prestamo_a_dto, dto_a_prestamo, fila_a_prestamo
from Dtos.Generico.Respuesta import Respuesta

class PrestamoServicio:

    def __init__(self):
        self.repositorio = PrestamoRepositorio()

    def insertarPrestamo(self, dto: PrestamoDTO) -> Respuesta:
        prestamo = dto_a_prestamo(dto)
        nuevo_id, codigo = self.repositorio.insertarPrestamo(prestamo)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(nuevo_id)
            nuevo = fila_a_prestamo(fila)
            return Respuesta("Operación Exitosa", "Préstamo registrado", [str(prestamo_a_dto(nuevo))])
        else:
            return Respuesta("Fallido", "No se pudo insertar el préstamo", [])

    def mostrarTodos(self) -> Respuesta:
        filas = self.repositorio.mostrarTodos()
        resultado = [str(prestamo_a_dto(fila_a_prestamo(f))) for f in filas]
        return Respuesta("Operación Exitosa", "Listado de préstamos", resultado)

    def mostrarPorId(self, dto: PrestamoDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.id)
        if fila:
            prestamo = fila_a_prestamo(fila)
            return Respuesta("Operación Exitosa", "Préstamo encontrado", [str(prestamo_a_dto(prestamo))])
        else:
            return Respuesta("Fallido", "Préstamo no encontrado", [])

    def actualizarPrestamo(self, dto: PrestamoDTO) -> Respuesta:
        prestamo = dto_a_prestamo(dto)
        codigo = self.repositorio.actualizarPrestamo(prestamo)
        if codigo == 1:
            fila = self.repositorio.mostrarPorId(prestamo.id)
            actualizado = fila_a_prestamo(fila)
            return Respuesta("Operación Exitosa", "Préstamo actualizado", [str(prestamo_a_dto(actualizado))])
        else:
            return Respuesta("Fallido", "No se pudo actualizar el préstamo", [])

    def borrarPrestamo(self, dto: PrestamoDTO) -> Respuesta:
        fila = self.repositorio.mostrarPorId(dto.id)
        if not fila:
            return Respuesta("Fallido", "Préstamo no existe", [])
        codigo = self.repositorio.borrarPrestamo(dto.id)
        if codigo == 1:
            prestamo = fila_a_prestamo(fila)
            return Respuesta("Operación Exitosa", "Préstamo eliminado", [str(prestamo_a_dto(prestamo))])
        else:
            return Respuesta("Fallido", "No se pudo eliminar el préstamo", [])
