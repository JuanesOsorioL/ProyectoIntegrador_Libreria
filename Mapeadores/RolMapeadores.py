from Entidades.Rol import Rol
from Dtos.RolDTO import RolDTO

def rol_a_dto(rol: Rol) -> RolDTO:
    return RolDTO(rol.GetId(), rol.GetNombre())

def dto_a_rol(dto: RolDTO) -> Rol:
    return Rol(dto.GetId(), dto.GetNombre(),None)

def fila_a_rol(fila: tuple) -> Rol:
    return Rol(fila[0], fila[1], fila[2])