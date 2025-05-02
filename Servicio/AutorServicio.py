from Dtos.AutorDTO import AutorDTO
from Entidades.Autor import Autor
from Mapeadores.Mapeadores import dto_a_autor, autor_a_dto, fila_a_autor
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.AutorRepositorio import AutorRepositorio

repositorio = AutorRepositorio()

EXITO = 1
AUTOR_EXISTE = 2

class AutorServicio:

    def insertarAutor(self, autorDTO: AutorDTO) -> Respuesta:
        try:
            autor = dto_a_autor(autorDTO)
            resultado = repositorio.insertarAutor(autor)
            nuevo_id, codigo = resultado
            if codigo == EXITO:
                nuevoAutor = Autor(id=nuevo_id, nombre="", nacionalidad="")
                resultadoAutor = repositorio.MostrarAutorPorId(nuevoAutor)
                autor_encontrado = fila_a_autor(resultadoAutor)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se guardó el nuevo autor",
                    resultado=[str(autor_a_dto(autor_encontrado))]
                )
            elif codigo == AUTOR_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="El autor ya existe",
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

    def MostrarTodosLosAutores(self) -> Respuesta:
        try:
            listaDTO = []
            lista = repositorio.MostrarTodosLosAutores()
            for item in lista:
                autor = Autor(id=item[0], nombre=item[1], nacionalidad=item[2])
                listaDTO.append(autor_a_dto(autor))
            if listaDTO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Existen autores registrados",
                    resultado=[str(dto) for dto in listaDTO]
                )
            else:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="No existen autores registrados",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al obtener autores: {str(ex)}",
                resultado=[]
            )

    def MostrarAutorPorId(self, autorDTO: AutorDTO) -> Respuesta:
        try:
            autor = dto_a_autor(autorDTO)
            resultado = repositorio.MostrarAutorPorId(autor)
            if resultado:
                autor_encontrado = fila_a_autor(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Autor encontrado",
                    resultado=[str(autor_a_dto(autor_encontrado))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe autor con ese ID",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al buscar autor: {str(ex)}",
                resultado=[]
            )

    def actualizarAutor(self, autorDTO: AutorDTO) -> Respuesta:
        try:
            autor = dto_a_autor(autorDTO)
            codigo = repositorio.actualizarAutor(autor)
            if codigo == EXITO:
                resultado = repositorio.MostrarAutorPorId(autor)
                autorActualizado = fila_a_autor(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Autor actualizado correctamente",
                    resultado=[str(autor_a_dto(autorActualizado))]
                )
            elif codigo == AUTOR_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró el autor con ese ID",
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
                msj=f"Error al actualizar autor: {str(ex)}",
                resultado=[]
            )

    def borrarAutor(self, autorDTO: AutorDTO) -> Respuesta:
        try:
            autor = dto_a_autor(autorDTO)
            autorExiste = repositorio.MostrarAutorPorId(autor)
            if not autorExiste:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe el autor a eliminar",
                    resultado=[]
                )
            codigo = repositorio.borrarAutor(autor)
            if codigo == EXITO:
                autorEliminado = fila_a_autor(autorExiste)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="El autor se eliminó correctamente",
                    resultado=[str(autor_a_dto(autorEliminado))]
                )
            elif codigo == AUTOR_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró el autor a eliminar",
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
                msj=f"Error al eliminar autor: {str(ex)}",
                resultado=[]
            )
