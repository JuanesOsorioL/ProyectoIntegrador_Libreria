from Servicio.LibroCategoriaServicio import LibroCategoriaServicio
from Dtos.LibroCategoriaDTO import LibroCategoriaDTO
from Dtos.Generico.Respuesta import Respuesta

libroCategoriaServicio: LibroCategoriaServicio = LibroCategoriaServicio()

class LibroCategoriaControlador:

    def insertarLibroCategoria(self, libro_id: int, categoria_id: int) -> Respuesta:
        libroCategoriaDTO = LibroCategoriaDTO(libro_id=libro_id, categoria_id=categoria_id)
        return libroCategoriaServicio.insertarLibroCategoria(libroCategoriaDTO)

    def mostrarTodosLosLibroCategoria(self) -> Respuesta:
        return libroCategoriaServicio.mostrarTodosLosLibroCategoria()

    def mostrarLibroCategoriaPorId(self, libro_id: int, categoria_id: int) -> Respuesta:
        libroCategoriaDTO = LibroCategoriaDTO(libro_id=libro_id, categoria_id=categoria_id)
        return libroCategoriaServicio.mostrarLibroCategoriaPorId(libroCategoriaDTO)

    def actualizarLibroCategoria(self, id: int, libro_id: int, categoria_id: int) -> Respuesta:
        libroCategoriaDTO = LibroCategoriaDTO()
        libroCategoriaDTO.id = id  # Suponiendo que haya un ID en la tabla intermedia, si no, omite esta línea.
        libroCategoriaDTO.libro_id = libro_id
        libroCategoriaDTO.categoria_id = categoria_id
        return libroCategoriaServicio.actualizarLibroCategoria(libroCategoriaDTO)
    
    #Nota: La función actualizarLibroCategoria solo tiene sentido si la tabla libro_categoria tiene un campo id único 
    # (como clave primaria artificial). Si estás usando una clave primaria compuesta (libro_id, categoria_id), 
    # entonces no es usual implementar una actualización (normalmente se elimina y se inserta un nuevo registro).

    def borrarLibroCategoria(self, libro_id: int, categoria_id: int) -> Respuesta:
        libroCategoriaDTO = LibroCategoriaDTO(libro_id=libro_id, categoria_id=categoria_id)
        return libroCategoriaServicio.borrarLibroCategoria(libroCategoriaDTO)