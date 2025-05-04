from Servicio.CategoriaServicio import CategoriaServicio
from Dtos.CategoriaDTO import CategoriaDTO
from Dtos.Generico.Respuesta import Respuesta

categoriaServicio: CategoriaServicio = CategoriaServicio()

class CategoriaControlador:

    def insertarCategoria(self, nombre: str) -> Respuesta:
        categoriaDTO = CategoriaDTO(id=None, nombre=nombre)
        return categoriaServicio.insertarCategoria(categoriaDTO)

    def mostrarTodasLasCategorias(self) -> Respuesta:
        return categoriaServicio.MostrarTodasLasCategorias()

    def mostrarCategoriaPorId(self, id: int) -> Respuesta:
        categoriaDTO = CategoriaDTO(id=id, nombre="")
        return categoriaServicio.MostrarCategoriaPorId(categoriaDTO)

    def actualizarCategoria(self, id: int, nombre: str) -> Respuesta:
        categoriaDTO = CategoriaDTO(id=id, nombre=nombre)
        return categoriaServicio.actualizarCategoria(categoriaDTO)

    def borrarCategoria(self, id: int) -> Respuesta:
        categoriaDTO = CategoriaDTO(id=id, nombre="")
        return categoriaServicio.borrarCategoria(categoriaDTO)