from Servicio.UsuarioServicio import UsuarioServicio
from Dtos.UsuarioDTO import UsuarioDTO
from Dtos.RolDTO import RolDTO
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Dtos.Generico.Respuesta import Respuesta

usuarioServicio= UsuarioServicio()

class UsuarioControlador:

    def insertarUsuario(nombre: str, email: str, telefono: str, direccion: str, rol_id: int,nombre_usuario: str, contrasena: str) -> Respuesta:
        roldto=RolDTO(rol_id,None)
        usuarioDTO = UsuarioDTO(None,nombre,email,telefono,direccion,None,rol_id,roldto)
        usuarioSistemaDTO=UsuarioSistemaDTO(None,None,nombre_usuario,contrasena,usuarioDTO)
        return usuarioServicio.insertar(usuarioSistemaDTO)













    def mostrarTodosLosUsuarios(self) -> Respuesta:
        return usuarioServicio.listar()

    def mostrarUsuarioPorId(self,id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(id,None,None,None,None,None,None)
        return usuarioServicio.obtenerPorId(usuarioDTO)

    def mostrarUsuarioPorEmail(self,email: str) -> Respuesta:
        usuarioDTO = UsuarioDTO(None,None,email,None,None,None,None)
        return usuarioServicio.obtenerPorEmail(usuarioDTO)
    
    def mostrarUsuarioPorRolId(self,id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(None,None,None,None,None,None,id)
        return usuarioServicio.obtenerPorRolId(usuarioDTO)

    def actualizarUsuario(self,id: int, nombre: str, email: str, telefono: str, direccion: str, fecha_registro: str, rol_id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(id,nombre,email,telefono,direccion,fecha_registro,rol_id)
        return usuarioServicio.actualizar(usuarioDTO)

    def borrarUsuario(self,id: int) -> Respuesta:
        usuarioDTO = UsuarioDTO(id,None,None,None,None,None,None)
        return usuarioServicio.borrar(usuarioDTO)