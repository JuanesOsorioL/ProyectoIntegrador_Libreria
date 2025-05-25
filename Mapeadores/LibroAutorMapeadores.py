from Dtos.LibroAutorDTO import LibroAutorDTO
from Entidades.LibroAutor import LibroAutor

def libro_autor_a_dto(libro_autor: LibroAutor) -> LibroAutorDTO:
    return LibroAutorDTO(id=libro_autor.id, id_libro=libro_autor.id_libro, id_autor=libro_autor.id_autor)

def dto_a_libro_autor(libro_autor_dto: LibroAutorDTO) -> LibroAutor:
    return LibroAutor(id=libro_autor_dto.id, id_libro=libro_autor_dto.id_libro, id_autor=libro_autor_dto.id_autor)

def fila_a_libro_autor(fila: tuple) -> LibroAutor:
    return LibroAutor(id=fila[0], id_libro=fila[1], id_autor=fila[2])