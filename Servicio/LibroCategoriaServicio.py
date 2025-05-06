from Dtos.LibroCategoriaDTO import LibroCategoriaDTO
from Entidades.LibroCategoria import LibroCategoria
from Mapeadores.Mapeadores import dto_a_libro_categoria, fila_a_libro_categoria, libro_categoria_a_dto
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.LibroCategoriaRepositorio import LibroCategoriaRepositorio

repositorio = LibroCategoriaRepositorio()

EXITO = 1
NO_EXISTE = 2
YA_EXISTE = 3

class LibroCategoriaServicio:

    def insertarLibroCategoria(self, dto: LibroCategoriaDTO) -> Respuesta:
        try:
            entidad = dto_a_libro_categoria(dto)
            resultado = repositorio.insertarLibroCategoria(entidad)
            codigo = resultado.respuesta if isinstance(resultado, tuple) and hasattr(resultado, 'respuesta') else resultado[0]
            
            if codigo == EXITO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se registró la relación libro-categoría",
                    resultado=[str(dto)]
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
                    msj="No se registró la relación",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al insertar libro-categoría: {str(ex)}",
                resultado=[]
            )

    def mostrarTodosLosLibroCategoria(self) -> Respuesta:
        try:
            lista = repositorio.mostrarTodosLosLibroCategoria()
            listaDTO = [libro_categoria_a_dto(fila_a_libro_categoria(f)) for f in lista]
            if listaDTO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relaciones encontradas",
                    resultado=[str(dto) for dto in listaDTO]
                )
            else:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="No hay relaciones registradas",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al listar relaciones: {str(ex)}",
                resultado=[]
            )

    def mostrarLibroCategoriaPorId(self, dto: LibroCategoriaDTO) -> Respuesta:
        try:
            entidad = dto_a_libro_categoria(dto)
            resultado = repositorio.mostrarLibroCategoriaPorId(entidad)
            if resultado:
                encontrado = fila_a_libro_categoria(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relación encontrada",
                    resultado=[str(libro_categoria_a_dto(encontrado))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe esa relación",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al consultar relación: {str(ex)}",
                resultado=[]
            )

    def actualizarLibroCategoria(self, dto_original: LibroCategoriaDTO, nuevo_libro_id: int, nueva_categoria_id: int) -> Respuesta:
        try:
            entidad = dto_a_libro_categoria(dto_original)
            codigo = repositorio.actualizarLibroCategoria(entidad, nuevo_libro_id, nueva_categoria_id)
            if codigo == EXITO:
                dto_nuevo = LibroCategoriaDTO(libro_id=nuevo_libro_id, categoria_id=nueva_categoria_id)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relación actualizada",
                    resultado=[str(dto_nuevo)]
                )
            elif codigo == NO_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe la relación original",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se actualizó la relación",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al actualizar: {str(ex)}",
                resultado=[]
            )

    def borrarLibroCategoria(self, dto: LibroCategoriaDTO) -> Respuesta:
        try:
            entidad = dto_a_libro_categoria(dto)
            existe = repositorio.mostrarLibroCategoriaPorId(entidad)
            if not existe:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe la relación a eliminar",
                    resultado=[]
                )
            codigo = repositorio.borrarLibroCategoria(entidad)
            if codigo == EXITO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Relación eliminada",
                    resultado=[str(dto)]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se eliminó la relación",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al eliminar: {str(ex)}",
                resultado=[]
            )