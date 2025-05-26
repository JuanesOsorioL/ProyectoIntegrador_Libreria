from Servicio.LibroServicio import LibroServicio
from Dtos.LibroDTO import LibroDTO
from Dtos.Generico.Respuesta import Respuesta

libroServicio = LibroServicio()

class LibroControlador:

    def insertarLibro(self, titulo, isbn, descripcion, anio_publicacion, formato, editorial_id, precio, stock) -> Respuesta:
        dto = LibroDTO(titulo=titulo, isbn=isbn, descripcion=descripcion, anio_publicacion=anio_publicacion,
                       formato=formato, editorial_id=editorial_id, precio=precio, stock=stock)
        return libroServicio.insertarLibro(dto)

    def mostrarTodos(self) -> Respuesta:
        return libroServicio.mostrarTodos()

    def mostrarPorId(self, id: int) -> Respuesta:
        dto = LibroDTO(id=id)
        return libroServicio.mostrarPorId(dto)

    def actualizarLibro(self, id, titulo, isbn, descripcion, anio_publicacion, formato, editorial_id, precio, stock) -> Respuesta:
        dto = LibroDTO(id=id, titulo=titulo, isbn=isbn, descripcion=descripcion, anio_publicacion=anio_publicacion,
                       formato=formato, editorial_id=editorial_id, precio=precio, stock=stock)
        return libroServicio.actualizarLibro(dto)

    def borrarLibro(self, id: int) -> Respuesta:
        dto = LibroDTO(id=id)
        return libroServicio.borrarLibro(dto)

