from Entidades.Rol import Rol
from Dtos.RolDTO import RolDTO

def rol_a_dto(rol: Rol) -> RolDTO:
    return RolDTO(id=rol.id, nombre=rol.nombre)

def dto_a_rol(rol_dto: RolDTO) -> Rol:
    return Rol(id=rol_dto.id, nombre=rol_dto.nombre)

def fila_a_rol(fila: tuple) -> Rol:
    return Rol(id=fila[0], nombre=fila[1])
