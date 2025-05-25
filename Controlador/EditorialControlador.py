from Servicio.EditorialServicio import EditorialServicio
from Dtos.EditorialDTO import EditorialDTO
from Dtos.Generico.Respuesta import Respuesta

editorialServicio: EditorialServicio = EditorialServicio()

class EditorialControlador:

    def insertarEditorial(self, nombre: str, pais: str) -> Respuesta:
        editorialDTO = EditorialDTO(id=None, nombre=nombre, pais=pais)
        return editorialServicio.insertarEditorial(editorialDTO)

    def mostrarTodasLasEditoriales(self) -> Respuesta:
        return editorialServicio.MostrarTodasLasEditoriales()

    def mostrarEditorialPorId(self, id: int) -> Respuesta:
        editorialDTO = EditorialDTO(id=id, nombre="", pais="")
        return editorialServicio.MostrarEditorialPorId(editorialDTO)

    def actualizarEditorial(self, id: int, nombre: str, pais: str) -> Respuesta:
        editorialDTO = EditorialDTO(id=id, nombre=nombre, pais=pais)
        return editorialServicio.actualizarEditorial(editorialDTO)

    def borrarEditorial(self, id: int) -> Respuesta:
        editorialDTO = EditorialDTO(id=id, nombre="", pais="")
        return editorialServicio.borrarEditorial(editorialDTO)
