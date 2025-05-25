from Entidades.Categoria import Categoria
from Dtos.CategoriaDTO import CategoriaDTO

def categoria_a_dto(categoria: Categoria) -> CategoriaDTO:
    return CategoriaDTO(id=categoria.id, nombre=categoria.nombre)

def dto_a_categoria(categoria_dto: CategoriaDTO) -> Categoria:
    return Categoria(id=categoria_dto.id, nombre=categoria_dto.nombre)

def fila_a_categoria(fila: tuple) -> Categoria:
    return Categoria(id=fila[0], nombre=fila[1])