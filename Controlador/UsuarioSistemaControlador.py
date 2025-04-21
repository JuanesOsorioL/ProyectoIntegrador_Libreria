from Servicio.UsuarioSistemaServicio import UsuarioSistemaServicio
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Dtos.Generico.Respuesta import Respuesta

usuarioSistemaServicio = UsuarioSistemaServicio()

class UsuarioSistemaControlador:

    def insertar(self, usuario_id: int, username: str, password_hash: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None,usuario_id,username,password_hash)
        return usuarioSistemaServicio.insertar(dto)

    def listar(self) -> Respuesta:
        return usuarioSistemaServicio.listar()

    def obtenerPorId(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None)
        return usuarioSistemaServicio.obtener_por_id(dto)

    def obtenerPorUsername(self, username: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None, None, username, None)
        return usuarioSistemaServicio.obtener_por_username(dto)

    def actualizar(self, id: int, usuario_id: int, username: str, password_hash: str) -> Respuesta:
        dto = UsuarioSistemaDTO(id,usuario_id,username,password_hash)
        return usuarioSistemaServicio.actualizar(dto)

    def eliminar(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None)
        return usuarioSistemaServicio.eliminar(dto)