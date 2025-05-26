from Dtos.LibroAutorDTO import LibroAutorDTO
from Entidades.LibroAutor import LibroAutor
from Mapeadores.LibroAutorMapeadores import dto_a_libro_autor, libro_autor_a_dto, fila_a_libro_autor
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
            if resultado == EXITO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se guardó la relación libro-autor",
                    resultado=(libro_autor_a_dto(libroAutorDTO)).to_dict_simple()
                )
            elif resultado == YA_EXISTE:
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
            print(lista)


            for item in lista:
                relacion = LibroAutor(item[0], item[1])
                listaDTO.append(libro_autor_a_dto(relacion).to_dict_simple())
            if listaDTO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Existen relaciones registradas",
                    resultado=[(dto) for dto in listaDTO]
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
            print(libroAutorDTO)
            resultado = repositorio.mostrarLibroAutorPorId(relacion)
            print(resultado)
            if resultado:
                encontrada = fila_a_libro_autor(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relación encontrada",
                    resultado=(libro_autor_a_dto(encontrada)).to_dict_simple()
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
            codigo = repositorio.actualizarLibroAutor(relacion,libroAutorDTO.GetAntesAutorId(),libroAutorDTO.GetAntesLibroId())
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
            print(libroAutorDTO)
            relacion = dto_a_libro_autor(libroAutorDTO)
            existe = repositorio.mostrarLibroAutorPorId(relacion)
            print(existe)
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
