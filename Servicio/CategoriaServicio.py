from Dtos.CategoriaDTO import CategoriaDTO
from Entidades.Categoria import Categoria
from Mapeadores.Mapeadores import dto_a_categoria, categoria_a_dto, fila_a_categoria
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.CategoriaRepositorio import CategoriaRepositorio

repositorio = CategoriaRepositorio()

EXITO = 1
CATEGORIA_EXISTE = 2

class CategoriaServicio:

    def insertarCategoria(self, categoriaDTO: CategoriaDTO) -> Respuesta:
        try:
            categoria = dto_a_categoria(categoriaDTO)
            resultado = repositorio.insertarCategoria(categoria)
            nuevo_id, codigo = resultado
            if codigo == EXITO:
                nuevaCategoria = Categoria(id=nuevo_id, nombre="")
                resultadoCategoria = repositorio.MostrarCategoriaPorId(nuevaCategoria)
                categoria_encontrada = fila_a_categoria(resultadoCategoria)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se guardó la nueva categoría",
                    resultado=[str(categoria_a_dto(categoria_encontrada))]
                )
            elif codigo == CATEGORIA_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="La categoría ya existe",
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

    def MostrarTodasLasCategorias(self) -> Respuesta:
        try:
            listaDTO = []
            lista = repositorio.MostrarTodasLasCategorias()
            for item in lista:
                categoria = Categoria(id=item[0], nombre=item[1])
                listaDTO.append(categoria_a_dto(categoria))
            if listaDTO:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Existen categorías registradas",
                    resultado=[str(dto) for dto in listaDTO]
                )
            else:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="No existen categorías registradas",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al obtener categorías: {str(ex)}",
                resultado=[]
            )

    def MostrarCategoriaPorId(self, categoriaDTO: CategoriaDTO) -> Respuesta:
        try:
            categoria = dto_a_categoria(categoriaDTO)
            resultado = repositorio.MostrarCategoriaPorId(categoria)
            if resultado:
                categoria_encontrada = fila_a_categoria(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Categoría encontrada",
                    resultado=[str(categoria_a_dto(categoria_encontrada))]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe categoría con ese ID",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al buscar categoría: {str(ex)}",
                resultado=[]
            )

    def actualizarCategoria(self, categoriaDTO: CategoriaDTO) -> Respuesta:
        try:
            categoria = dto_a_categoria(categoriaDTO)
            codigo = repositorio.actualizarCategoria(categoria)
            if codigo == EXITO:
                resultado = repositorio.MostrarCategoriaPorId(categoria)
                categoriaActualizada = fila_a_categoria(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Categoría actualizada correctamente",
                    resultado=[str(categoria_a_dto(categoriaActualizada))]
                )
            elif codigo == CATEGORIA_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró la categoría con ese ID",
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
                msj=f"Error al actualizar categoría: {str(ex)}",
                resultado=[]
            )

    def borrarCategoria(self, categoriaDTO: CategoriaDTO) -> Respuesta:
        try:
            categoria = dto_a_categoria(categoriaDTO)
            categoriaExiste = repositorio.MostrarCategoriaPorId(categoria)
            if not categoriaExiste:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe la categoría a eliminar",
                    resultado=[]
                )
            codigo = repositorio.borrarCategoria(categoria)
            if codigo == EXITO:
                categoriaEliminada = fila_a_categoria(categoriaExiste)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="La categoría se eliminó correctamente",
                    resultado=[str(categoria_a_dto(categoriaEliminada))]
                )
            elif codigo == CATEGORIA_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró la categoría a eliminar",
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
                msj=f"Error al eliminar categoría: {str(ex)}",
                resultado=[]
            )
