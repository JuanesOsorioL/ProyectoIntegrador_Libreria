from Servicio.LibroAutorServicio import LibroAutorServicio
from Dtos.LibroAutorDTO import LibroAutorDTO
from Dtos.Generico.Respuesta import Respuesta

libroAutorServicio: LibroAutorServicio = LibroAutorServicio()

class LibroAutorControlador:

    def insertarLibroAutor(self, libro_id: int, autor_id: int) -> Respuesta:
        libroAutorDTO = LibroAutorDTO(libro_id=libro_id, autor_id=autor_id)
        return libroAutorServicio.insertarLibroAutor(libroAutorDTO)

    def mostrarTodosLosLibroAutor(self) -> Respuesta:
        return libroAutorServicio.mostrarTodosLosLibroAutor()

    def mostrarLibroAutorPorId(self, libro_id: int, autor_id: int) -> Respuesta:
        libroAutorDTO = LibroAutorDTO(libro_id=libro_id, autor_id=autor_id)
        return libroAutorServicio.mostrarLibroAutorPorId(libroAutorDTO)
    
    def actualizarLibroAutor(self, id: int, libro_id: int, autor_id: int) -> Respuesta:
        libroAutorDTO = LibroAutorDTO(id=id, libro_id=libro_id, autor_id=autor_id)
        return libroAutorServicio.actualizarLibroAutor(libroAutorDTO)

    def borrarLibroAutor(self, libro_id: int, autor_id: int) -> Respuesta:
        libroAutorDTO = LibroAutorDTO(libro_id=libro_id, autor_id=autor_id)
        return libroAutorServicio.borrarLibroAutor(libroAutorDTO)
