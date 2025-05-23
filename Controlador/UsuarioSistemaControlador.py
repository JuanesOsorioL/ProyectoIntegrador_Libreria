from Servicio.UsuarioSistemaServicio import UsuarioSistemaServicio
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Dtos.Generico.Respuesta import Respuesta

usuarioSistemaServicio = UsuarioSistemaServicio()

class UsuarioSistemaControlador:

    def obtenerPorNombreUsuarioYContrasena(self,nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None, None, nombre_usuario, contrasena, None)
        return usuarioSistemaServicio.obtenerPorUsernameYContrasena(dto)

    def listarUsuariosSistema(self) -> Respuesta:
        return usuarioSistemaServicio.listarUsuariosistema()
    
    def obtenerUsuariosSistemaPorId(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None, None)
        return usuarioSistemaServicio.obtenerUsuarioSistemaPorId(dto)

    def obtenerPorNombreUsuario(self, nombre_usuario: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None, None, nombre_usuario, None, None)
        return usuarioSistemaServicio.obtenerPorUsernameConRespuesta(dto)
    
    def eliminarNombreUsuario(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None, None)
        return usuarioSistemaServicio.eliminarNombreUsuario(dto)

    def actualizarUsuarioSistemaPorId(self, id: int, nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(id,None,nombre_usuario,contrasena, None)
        return usuarioSistemaServicio.actualizarUsuarioSistemaPorId(dto)