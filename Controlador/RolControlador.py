from Servicio.RolServicio import RolServicio
from Dtos.RolDTO import RolDTO
from Dtos.Generico.Respuesta import Respuesta

rolServicio:RolServicio=RolServicio();

class RolControlador:
    
    def insertarRol(self, nombre: str) -> Respuesta:
        rolDTO = RolDTO(id=None, nombre=nombre)
        return rolServicio.insertarRol(rolDTO)
    
    def mostrarTodosLosRoles(self) -> Respuesta:
        return rolServicio.MostrarTodosLosRoles()

    def mostrarRolPorId(self, id:int) -> Respuesta:
        rolDTO = RolDTO(id=id, nombre="")
        return rolServicio.MostrarRolPorId(rolDTO)

    def actualizarRol(self, id:int, nombre:str) -> Respuesta:
        rolDTO = RolDTO(id=id, nombre=nombre)
        return rolServicio.actualizarRol(rolDTO)

    def borrarRol(self, id:int) -> Respuesta:
        rolDTO = RolDTO(id=id, nombre="")
        return rolServicio.borrarRol(rolDTO)