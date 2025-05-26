from Dtos.LibroDTO import LibroDTO
from Repositorios.LibroRepositorio import LibroRepositorio
from Mapeadores.Mapeadores import libro_a_dto, dto_a_libro, fila_a_libro
from Dtos.Generico.Respuesta import Respuesta

repositorio = LibroRepositorio()

class LibroServicio:

    def insertarLibro(self, dto: LibroDTO) -> Respuesta:
        try:
            libro = dto_a_libro(dto)
            nuevo_id, codigo = repositorio.insertarLibro(libro)
            if codigo == 1:
                fila = repositorio.mostrarPorId(nuevo_id)
                libro_insertado = fila_a_libro(fila)
                return Respuesta("Éxito", "Libro guardado", [str(libro_a_dto(libro_insertado))])
            elif codigo == 2:
                return Respuesta("Fallido", "El libro ya existe", [])
            else:
                return Respuesta("Error", "Error al insertar", [])
        except ValueError as e:
            return Respuesta("Error de datos", str(e), [])
        except Exception as e:
            return Respuesta("Error inesperado", f"Ocurrió un error al insertar: {str(e)}", [])

    def mostrarTodos(self) -> Respuesta:
        lista = repositorio.mostrarTodos()
        if lista:
            return Respuesta("Éxito", "Lista de libros", [str(libro_a_dto(fila_a_libro(f))) for f in lista])
        else:
            return Respuesta("Éxito", "No hay libros", [])

    def mostrarPorId(self, dto: LibroDTO) -> Respuesta:
        fila = repositorio.mostrarPorId(dto.id)
        if fila:
            return Respuesta("Éxito", "Libro encontrado", [str(libro_a_dto(fila_a_libro(fila)))])
        else:
            return Respuesta("Fallido", "No existe ese libro", [])
        
    def actualizarLibro(self, dto: LibroDTO) -> Respuesta:
        try:
            libro = dto_a_libro(dto)
            codigo = repositorio.actualizarLibro(libro)
            if codigo == 1:
                fila = repositorio.mostrarPorId(libro.id)
                actualizado = fila_a_libro(fila)
                return Respuesta("Éxito", "Libro actualizado", [str(libro_a_dto(actualizado))])
            else:
                return Respuesta("Fallido", "No se pudo actualizar", [])
        except ValueError as e:
            return Respuesta("Error de datos", str(e), [])
        except Exception as e:
            return Respuesta("Error inesperado", f"Ocurrió un error al actualizar: {str(e)}", [])

    def borrarLibro(self, dto: LibroDTO) -> Respuesta:
        fila = repositorio.mostrarPorId(dto.id)
        if not fila:
            return Respuesta("Fallido", "No existe el libro", [])
        codigo = repositorio.borrarLibro(dto.id)
        if codigo == 1:
            eliminado = fila_a_libro(fila)
            return Respuesta("Éxito", "Libro eliminado", [str(libro_a_dto(eliminado))])
        else:
            return Respuesta("Fallido", "No se pudo eliminar", [])
