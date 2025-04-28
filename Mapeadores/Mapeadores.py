from Entidades.Rol import Rol
from Dtos.RolDTO import RolDTO

from Entidades.Editorial import Editorial
from Dtos.EditorialDTO import EditorialDTO

from Entidades.Devolucion import Devolucion
from Dtos.DevolucionDTO import DevolucionDTO


"""Mapeador Rol"""
def rol_a_dto(rol: Rol) -> RolDTO:
    return RolDTO(id=rol.id, nombre=rol.nombre)

def dto_a_rol(rol_dto: RolDTO) -> Rol:
    return Rol(id=rol_dto.id, nombre=rol_dto.nombre)

def fila_a_rol(fila: tuple) -> Rol:
    return Rol(id=fila[0], nombre=fila[1])


"""Mapeador Editorial"""

def editorial_a_dto(editorial: Editorial) -> EditorialDTO:
    """Convierte una entidad Editorial en un DTO EditorialDTO."""
    return EditorialDTO(id=editorial.id, nombre=editorial.nombre, pais=editorial.pais)

def dto_a_editorial(editorial_dto: EditorialDTO) -> Editorial:
    """Convierte un DTO EditorialDTO en una entidad Editorial."""
    return Editorial(id=editorial_dto.id, nombre=editorial_dto.nombre, pais=editorial_dto.pais)

def fila_a_editorial(fila: tuple) -> Editorial:
    """Convierte una fila de la base de datos (tupla) en una entidad Editorial."""
    return Editorial(id=fila[0], nombre=fila[1], pais=fila[2])


def devolucion_a_dto(dev: Devolucion) -> DevolucionDTO:
    return DevolucionDTO(
        id=dev.id,
        fecha_real_devolucion=dev.fecha_real_devolucion,
        estado_libro=dev.estado_libro,
        observaciones=dev.observaciones
    )

def dto_a_devolucion(dto: DevolucionDTO) -> Devolucion:
    return Devolucion(
        id=dto.id,
        fecha_real_devolucion=dto.fecha_real_devolucion,
        estado_libro=dto.estado_libro,
        observaciones=dto.observaciones
    )

def fila_a_devolucion(fila: tuple) -> Devolucion:
    return Devolucion(
        id=fila[0],
        fecha_real_devolucion=fila[1],
        estado_libro=fila[2],
        observaciones=fila[3]
    )

