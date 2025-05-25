from Dtos.LibroAutorDTO import LibroAutorDTO
from Entidades.LibroAutor import LibroAutor
from Mapeadores.Mapeadores import dto_a_libro_autor, libro_autor_a_dto, fila_a_libro_autor
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.LibroAutorRepositorio import LibroAutorRepositorio

repositorio = LibroAutorRepositorio()

EXITO = 1
YA_EXISTE = 2

class LibroAutorServicio:

    def insertarLibroAutor(self, libroAutorDTO: LibroAutorDTO) -> Respuesta:
        try:
            libro_autor = dto_a_libro_autor(libroAutorDTO)
            resultado = repositorio.insertarLibroAutor(libro_autor)
            nuevo_id, codigo = resultado
            if codigo == EXITO:
                nuevoRelacion = LibroAutor(id=nuevo_id, id_libro=libroAutorDTO.id_libro, id_autor=libroAutorDTO.id_autor)
                resultadoRelacion = repositorio.mostrarLibroAutorPorId(nuevoRelacion)
                relacion_encontrada = fila_a_libro_autor(resultadoRelacion)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se guardó la relación libro-autor",
                    resultado=[str(libro_autor_a_dto(relacion_encontrada))]
                )
            elif codigo == YA_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="La relación ya existe",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se realizó el guardado",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error en la inserción: {ex}",
                resultado=[]
            )

    def mostrarTodosLosLibroAutor(self) -> Respuesta:
        try:
            listaDTO = []
            lista = repositorio.mostrarTodosLosLibroAutor()
            for item in lista:
                relacion = LibroAutor(id=item[0], id_libro=item[1], id_autor=item[2])
                listaDTO.append(libro_autor_a_dto(relacion))
            if listaDTO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Existen relaciones registradas",
                    resultado=[str(dto) for dto in listaDTO]
                )
            else:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="No existen relaciones registradas",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al obtener relaciones: {str(ex)}",
                resultado=[]
            )

    def mostrarLibroAutorPorId(self, libroAutorDTO: LibroAutorDTO) -> Respuesta:
        try:
            relacion = dto_a_libro_autor(libroAutorDTO)
            resultado = repositorio.mostrarLibroAutorPorId(relacion)
            if resultado:
                encontrada = fila_a_libro_autor(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relación encontrada",
                    resultado=[str(libro_autor_a_dto(encontrada))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe relación con ese ID",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al buscar relación: {str(ex)}",
                resultado=[]
            )

    def actualizarLibroAutor(self, libroAutorDTO: LibroAutorDTO) -> Respuesta:
        try:
            relacion = dto_a_libro_autor(libroAutorDTO)
            codigo = repositorio.actualizarLibroAutor(relacion)
            if codigo == EXITO:
                resultado = repositorio.mostrarLibroAutorPorId(relacion)
                actualizada = fila_a_libro_autor(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relación actualizada correctamente",
                    resultado=[str(libro_autor_a_dto(actualizada))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró la relación con ese ID",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al actualizar relación: {str(ex)}",
                resultado=[]
            )

    def borrarLibroAutor(self, libroAutorDTO: LibroAutorDTO) -> Respuesta:
        try:
            relacion = dto_a_libro_autor(libroAutorDTO)
            existe = repositorio.mostrarLibroAutorPorId(relacion)
            if not existe:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe la relación a eliminar",
                    resultado=[]
                )
            codigo = repositorio.borrarLibroAutor(relacion)
            if codigo == EXITO:
                eliminada = fila_a_libro_autor(existe)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="La relación se eliminó correctamente",
                    resultado=[str(libro_autor_a_dto(eliminada))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró la relación a eliminar",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al eliminar relación: {str(ex)}",
                resultado=[]
            )
