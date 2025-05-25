from Entidades.LibroCategoria import LibroCategoria
from Dtos.LibroCategoriaDTO import LibroCategoriaDTO

def libro_categoria_a_dto(libro_categoria: LibroCategoria) -> LibroCategoriaDTO:
    return LibroCategoriaDTO(libro_id=libro_categoria.libro_id, categoria_id=libro_categoria.categoria_id)

def dto_a_libro_categoria(libro_categoria_dto: LibroCategoriaDTO) -> LibroCategoria:
    return LibroCategoria(libro_id=libro_categoria_dto.libro_id, categoria_id=libro_categoria_dto.categoria_id)

def fila_a_libro_categoria(fila: tuple) -> LibroCategoria:
    return LibroCategoria(libro_id=fila[0], categoria_id=fila[1])