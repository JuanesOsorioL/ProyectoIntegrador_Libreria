from Dtos.LibroAutorDTO import LibroAutorDTO
from Entidades.LibroAutor import LibroAutor

def libro_autor_a_dto(libro_autor: LibroAutor) -> LibroAutorDTO:
    return LibroAutorDTO(libro_autor.GetLibroId(),libro_autor.GetAutorId())

def dto_a_libro_autor(dto: LibroAutorDTO) -> LibroAutor:
    return LibroAutor(dto.GetLibroId(),dto.GetAutorId())

def fila_a_libro_autor(fila: tuple) -> LibroAutor:
    return LibroAutor(fila[0], fila[1])