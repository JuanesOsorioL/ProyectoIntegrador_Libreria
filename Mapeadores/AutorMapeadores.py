from Entidades.Autor import Autor
from Dtos.AutorDTO import AutorDTO

def autor_a_dto(autor: Autor) -> AutorDTO:
    return AutorDTO(id=autor.id, nombre=autor.nombre, nacionalidad=autor.nacionalidad)

def dto_a_autor(autor_dto: AutorDTO) -> Autor:
    return Autor(id=autor_dto.id, nombre=autor_dto.nombre, nacionalidad=autor_dto.nacionalidad)

def fila_a_autor(fila: tuple) -> Autor:
    return Autor(id=fila[0], nombre=fila[1], nacionalidad=fila[2])