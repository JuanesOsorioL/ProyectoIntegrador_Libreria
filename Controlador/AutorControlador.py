from Servicio.AutorServicio import AutorServicio
from Dtos.AutorDTO import AutorDTO
from Dtos.Generico.Respuesta import Respuesta

autorServicio: AutorServicio = AutorServicio()

class AutorControlador:

    def insertarAutor(self, nombre: str, nacionalidad: str) -> Respuesta:
        autorDTO = AutorDTO(id=None, nombre=nombre, nacionalidad=nacionalidad)
        return autorServicio.insertarAutor(autorDTO)

    def mostrarTodosLosAutores(self) -> Respuesta:
        return autorServicio.MostrarTodosLosAutores()

    def mostrarAutorPorId(self, id: int) -> Respuesta:
        autorDTO = AutorDTO(id=id, nombre="", nacionalidad="")
        return autorServicio.MostrarAutorPorId(autorDTO)

    def actualizarAutor(self, id: int, nombre: str, nacionalidad: str) -> Respuesta:
        autorDTO = AutorDTO(id=id, nombre=nombre, nacionalidad=nacionalidad)
        return autorServicio.actualizarAutor(autorDTO)

    def borrarAutor(self, id: int) -> Respuesta:
        autorDTO = AutorDTO(id=id, nombre="", nacionalidad="")
        return autorServicio.borrarAutor(autorDTO)