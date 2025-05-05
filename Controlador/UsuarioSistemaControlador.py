from Servicio.UsuarioSistemaServicio import UsuarioSistemaServicio
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Dtos.Generico.Respuesta import Respuesta

usuarioSistemaServicio = UsuarioSistemaServicio()

class UsuarioSistemaControlador:

    def insertar(self, usuario_id: int, nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None,usuario_id,nombre_usuario,contrasena)
        return usuarioSistemaServicio.insertar(dto)

    def listar(self) -> Respuesta:
        return usuarioSistemaServicio.listar()

    def obtenerPorId(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None)
        return usuarioSistemaServicio.obtener_por_id(dto)

    def obtenerPorNombreUsuario(self, nombre_usuario: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None, None, nombre_usuario, None)
        return usuarioSistemaServicio.obtenerPorUsername(dto)

    def actualizar(self, id: int, usuario_id: int, nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(id,usuario_id,nombre_usuario,contrasena)
        return usuarioSistemaServicio.actualizar(dto)

    def eliminar(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None)
        return usuarioSistemaServicio.eliminar(dto)