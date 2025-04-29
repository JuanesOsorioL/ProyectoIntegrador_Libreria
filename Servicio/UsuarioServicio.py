from Dtos.UsuarioDTO import UsuarioDTO
from Entidades.Usuario import Usuario
from Mapeadores.UsuarioMapeadores import usuario_a_dto, dto_a_usuario, fila_a_usuario
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.UsuarioRepositorio import UsuarioRepositorio

repositorio = UsuarioRepositorio()

EXITO = 1
YA_EXISTE = 2

class UsuarioServicio:

    def insertar(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            resultado = repositorio.insertar_Usuario(usuario)
            nuevo_id, codigo = resultado

            if codigo == EXITO:
                usuario_insertado = Usuario()
                usuario_insertado.Set_Id(nuevo_id)
                fila = repositorio.mostrar_Usuario_por_id(usuario_insertado)
                if fila:
                    usuarioDto = usuario_a_dto(fila_a_usuario(fila))
                    return Respuesta("Operación Exitosa", "Usuario registrado", usuarioDto)
                else:
                    return Respuesta("Operación Fallida", "Usuario no encontrado luego de insertar", [])
            elif codigo == YA_EXISTE:
                return Respuesta("Operación Fallida", "El usuario ya existe", [])
            
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al registrar usuario: {ex}", [])

    def listar(self) -> Respuesta:
        try:
            lista = repositorio.mostrar_todos_los_Usuarios()
            usuarios = [str(usuario_a_dto(fila_a_usuario(f))) for f in lista]
            if usuarios:
                return Respuesta("Operación Exitosa", "Usuarios encontrados", usuarios)
            else:
                return Respuesta("Operación Exitosa", "No hay usuarios registrados", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al listar usuarios: {ex}", [])

    def obtener_por_id(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            fila = repositorio.mostrar_Usuario_por_id(usuario)
            if fila:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                return Respuesta("Operación Exitosa", "Usuario encontrado", [str(dto_resultado)])
            return Respuesta("Operación Fallida", "No existe usuario con ese ID", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar usuario por ID: {ex}", [])

    def obtener_por_email(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            fila = repositorio.mostrar_Usuario_por_email(usuario)
            if fila:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                return Respuesta("Operación Exitosa", "Usuario encontrado", [str(dto_resultado)])
            return Respuesta("Operación Fallida", "No existe usuario con ese correo", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar usuario por correo: {ex}", [])

    def actualizar(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            codigo = repositorio.actualizar_Usuario(usuario)
            if codigo == EXITO:
                fila = repositorio.mostrar_Usuario_por_id(usuario)
                if fila:
                    dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                    return Respuesta("Operación Exitosa", "Usuario actualizado correctamente", [str(dto_resultado)])
                else:
                    return Respuesta("Operación Fallida", "Usuario no encontrado luego de actualizar", [])
            return Respuesta("Operación Fallida", "No se pudo actualizar", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al actualizar usuario: {ex}", [])

    def borrar(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            fila = repositorio.mostrar_Usuario_por_id(usuario)
            if not fila:
                return Respuesta("Operación Fallida", "No existe el usuario a eliminar", [])
            codigo = repositorio.borrar_Usuario(usuario)
            if codigo == EXITO:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                return Respuesta("Operación Exitosa", "Usuario eliminado", [str(dto_resultado)])
            return Respuesta("Operación Fallida", "No se pudo eliminar el usuario", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al eliminar usuario: {ex}", [])
        
    def obtener_por_rol_id(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            lista = repositorio.mostrar_Usuario_por_rol_id(usuario)
            usuarios = [str(usuario_a_dto(fila_a_usuario(f))) for f in lista]
            if usuarios:
                return Respuesta("Operación Exitosa", "Usuario encontrado con el mismo Rol ID", usuarios)
            return Respuesta("Operación Fallida", "No existen usuarios con ese Rol ID", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar usuario por Rol ID: {ex}", [])