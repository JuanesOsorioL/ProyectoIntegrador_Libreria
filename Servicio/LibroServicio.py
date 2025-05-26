from Dtos.LibroDTO import LibroDTO
from Repositorios.LibroRepositorio import LibroRepositorio
from Mapeadores.LibroMapeadores import libro_a_dto, dto_a_libro, fila_a_libro
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
                return Respuesta("Operación Exitosa", "Libro guardado", libro_a_dto(libro_insertado).to_dict_simple())
            elif codigo == 2:
                return Respuesta("Operación Fallida", "El libro ya existe", [])
            else:
                return Respuesta("Error Sistema", "Error al insertar", [])
        except ValueError as e:
            return Respuesta("Error Sistema", str(e), [])
        except Exception as e:
            return Respuesta("Error Sistema", f"Ocurrió un error al insertar: {str(e)}", [])

    def mostrarTodos(self) -> Respuesta:
        lista = repositorio.mostrarTodos()
        if lista:
            return Respuesta("Operación Exitosa", "Lista de libros", [libro_a_dto(fila_a_libro(f)).to_dict_simple() for f in lista])
        else:
            return Respuesta("Operación Exitosa", "No hay libros", [])

    def mostrarPorId(self, dto: LibroDTO) -> Respuesta:
        fila = repositorio.mostrarPorId(dto.id)
        if fila:
            return Respuesta("Operación Exitosa", "Libro encontrado", libro_a_dto(fila_a_libro(fila)).to_dict_simple())
        else:
            return Respuesta("Operación Fallida", "No existe ese libro", [])
        
    def actualizarLibro(self, dto: LibroDTO) -> Respuesta:
        try:
            libro = dto_a_libro(dto)
            codigo = repositorio.actualizarLibro(libro)
            if codigo == 1:
                fila = repositorio.mostrarPorId(libro.id)
                actualizado = fila_a_libro(fila)
                return Respuesta("Operación Exitosa", "Libro actualizado", libro_a_dto(actualizado).to_dict_simple())
            else:
                return Respuesta("Operación Fallida", "No se pudo actualizar", [])
        except ValueError as e:
            return Respuesta("Error de datos", str(e), [])
        except Exception as e:
            return Respuesta("Error inesperado", f"Ocurrió un error al actualizar: {str(e)}", [])

    def borrarLibro(self, dto: LibroDTO) -> Respuesta:
        fila = repositorio.mostrarPorId(dto.id)
        if not fila:
            return Respuesta("Operación Fallida", "No existe el libro", [])
        codigo = repositorio.borrarLibro(dto.id)
        if codigo == 1:
            eliminado = fila_a_libro(fila)
            return Respuesta("Operación Exitosa", "Libro eliminado", libro_a_dto(eliminado).to_dict_simple())
        else:
            return Respuesta("Operación Fallida", "No se pudo eliminar", [])
