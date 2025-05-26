from Entidades.Libro import Libro
from Dtos.LibroDTO import LibroDTO

def libro_a_dto(libro: Libro) -> LibroDTO:
    return LibroDTO(
        id=libro.id,
        titulo=libro.titulo,
        isbn=libro.isbn,
        descripcion=libro.descripcion,
        anio_publicacion=libro.anio_publicacion,
        formato=libro.formato,
        editorial_id=libro.editorial_id,
        precio=libro.precio,
        stock=libro.stock
    )

def dto_a_libro(dto: LibroDTO) -> Libro:
    return Libro(
        id=dto.id,
        titulo=dto.titulo,
        isbn=dto.isbn,
        descripcion=dto.descripcion,
        anio_publicacion=dto.anio_publicacion,
        formato=dto.formato,
        editorial_id=dto.editorial_id,
        precio=dto.precio,
        stock=dto.stock
    )

def fila_a_libro(fila: tuple) -> Libro:
    return Libro(*fila)