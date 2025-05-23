from Servicio.RolServicio import RolServicio
from Dtos.RolDTO import RolDTO
from Dtos.Generico.Respuesta import Respuesta

rolServicio=RolServicio();

class RolControlador:

    def mostrarTodosLosRoles(self) -> Respuesta:
        return rolServicio.MostrarTodosLosRoles()
    
    def mostrarRolPorId(self, id:int) -> Respuesta:
        rolDTO = RolDTO(id, None)
        return rolServicio.MostrarRolPorId(rolDTO)
    
    def actualizarRol(self, id:int, nombre:str) -> Respuesta:
        rolDTO = RolDTO(id, nombre)
        return rolServicio.actualizarRol(rolDTO)
    
    def borrarRol(self, id:int) -> Respuesta:
        rolDTO = RolDTO(id, None)
        return rolServicio.borrarRol(rolDTO)
    
    def InsertarNuevoRol(self, nombre:str) -> Respuesta:
        rolDTO = RolDTO(None, nombre)
        return rolServicio.insertarNuevoRol(rolDTO)