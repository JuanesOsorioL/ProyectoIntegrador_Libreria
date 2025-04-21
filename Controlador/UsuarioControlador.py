from Servicio.UsuarioServicio import UsuarioServicio
from Dtos.UsuarioDTO import UsuarioDTO
from Dtos.Generico.Respuesta import Respuesta

usuarioServicio: UsuarioServicio = UsuarioServicio()

class UsuarioControlador:

    def insertarUsuario(self, nombre: str, email: str, telefono: str, direccion: str, fecha_registro: str, rol_id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(None,nombre,email,telefono,direccion,fecha_registro,rol_id)
        return usuarioServicio.insertar(usuarioDTO)

    def mostrarTodosLosUsuarios(self) -> Respuesta:
        return usuarioServicio.listar()

    def mostrarUsuarioPorId(self, id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(id,None,None,None,None,None,None)
        return usuarioServicio.obtener_por_id(usuarioDTO)

    def mostrarUsuarioPorEmail(self, email: str) -> Respuesta:
        usuarioDTO = UsuarioDTO(None,None,email,None,None,None,None)
        return usuarioServicio.obtener_por_email(usuarioDTO)

    def actualizarUsuario(self, id: int, nombre: str, email: str, telefono: str, direccion: str, fecha_registro: str, rol_id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(id,nombre,email,telefono,direccion,fecha_registro,rol_id)
        return usuarioServicio.actualizar(usuarioDTO)

    def borrarUsuario(self, id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(id,None,None,None,None,None,None)
        return usuarioServicio.borrar(usuarioDTO)
    
    def mostrarUsuarioPorRolId(self, id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(None,None,None,None,None,None,id)
        return usuarioServicio.obtener_por_rol_id(usuarioDTO)