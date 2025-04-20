from Dtos.EditorialDTO import EditorialDTO
from Entidades.Editorial import Editorial
from Mapeadores.Mapeadores import dto_a_editorial, editorial_a_dto, fila_a_editorial
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.EditorialRepositorio import EditorialRepositorio

repositorio = EditorialRepositorio()

EXITO = 1
EDITORIAL_EXISTE = 2

class EditorialServicio:

    def insertarEditorial(self, editorialDTO: EditorialDTO) -> Respuesta:
        try:
            editorial = dto_a_editorial(editorialDTO)
            resultado = repositorio.insertarEditorial(editorial)
            nuevo_id, codigo = resultado
            if codigo == EXITO:
                nuevaEditorial = Editorial(id=nuevo_id, nombre="", pais="")
                resultadoEditorial = repositorio.MostrarEditorialPorId(nuevaEditorial)
                editorial_encontrada = fila_a_editorial(resultadoEditorial)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se guardó la nueva Editorial",
                    resultado=[str(editorial_a_dto(editorial_encontrada))]
                )
            elif codigo == EDITORIAL_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="La editorial ya existe",
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

    def MostrarTodasLasEditoriales(self) -> Respuesta:
        try:
            listaDTO = []
            lista = repositorio.MostrarTodasLasEditoriales()
            for item in lista:
                editorial = Editorial(id=item[0], nombre=item[1], pais=item[2])
                listaDTO.append(editorial_a_dto(editorial))
            if listaDTO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Existen editoriales registradas",
                    resultado=[str(dto) for dto in listaDTO]
                )
            else:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="No existen editoriales registradas",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al obtener editoriales: {str(ex)}",
                resultado=[]
            )

    def MostrarEditorialPorId(self, editorialDTO: EditorialDTO) -> Respuesta:
        try:
            editorial = dto_a_editorial(editorialDTO)
            resultado = repositorio.MostrarEditorialPorId(editorial)
            if resultado:
                editorial_encontrada = fila_a_editorial(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Editorial encontrada",
                    resultado=[str(editorial_a_dto(editorial_encontrada))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe editorial con ese ID",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al buscar editorial: {str(ex)}",
                resultado=[]
            )

    def actualizarEditorial(self, editorialDTO: EditorialDTO) -> Respuesta:
        try:
            editorial = dto_a_editorial(editorialDTO)
            codigo = repositorio.actualizarEditorial(editorial)
            if codigo == EXITO:
                resultado = repositorio.MostrarEditorialPorId(editorial)
                editorialActualizada = fila_a_editorial(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Editorial actualizada correctamente",
                    resultado=[str(editorial_a_dto(editorialActualizada))]
                )
            elif codigo == EDITORIAL_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró la editorial con ese ID",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj=f"Código inesperado: {codigo}",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al actualizar editorial: {str(ex)}",
                resultado=[]
            )

    def borrarEditorial(self, editorialDTO: EditorialDTO) -> Respuesta:
        try:
            editorial = dto_a_editorial(editorialDTO)
            editorialExiste = repositorio.MostrarEditorialPorId(editorial)
            if not editorialExiste:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe la editorial a eliminar",
                    resultado=[]
                )
            codigo = repositorio.borrarEditorial(editorial)
            if codigo == EXITO:
                editorialEliminada = fila_a_editorial(editorialExiste)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="La editorial se eliminó correctamente",
                    resultado=[str(editorial_a_dto(editorialEliminada))]
                )
            elif codigo == EDITORIAL_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró la editorial a eliminar",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj=f"Código inesperado: {codigo}",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al eliminar editorial: {str(ex)}",
                resultado=[]
            )
