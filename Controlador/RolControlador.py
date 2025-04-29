from Servicio.RolServicio import RolServicio
from Dtos.RolDTO import RolDTO
from Dtos.Generico.Respuesta import Respuesta

rolServicio:RolServicio=RolServicio();

class RolControlador:
    
    def insertarRol(self, nombre: str) -> Respuesta:
        rolDTO = RolDTO(None, nombre)
        return rolServicio.insertarRol(rolDTO)
    
    def mostrarTodosLosRoles(self) -> Respuesta:
        return rolServicio.MostrarTodosLosRoles()
    
    def mostrarTodosLosRolesSeleccionar(self) -> list:
        return rolServicio.MostrarTodosLosRolesSeleccionar()

    def mostrarRolPorId(self, id:int) -> Respuesta:
        rolDTO = RolDTO(id=id, nombre="")
        return rolServicio.MostrarRolPorId(rolDTO)

    def actualizarRol(self, id:int, nombre:str) -> Respuesta:
        rolDTO = RolDTO(id=id, nombre=nombre)
        return rolServicio.actualizarRol(rolDTO)

    def borrarRol(self, id:int) -> Respuesta:
        rolDTO = RolDTO(id=id, nombre="")
        return rolServicio.borrarRol(rolDTO)