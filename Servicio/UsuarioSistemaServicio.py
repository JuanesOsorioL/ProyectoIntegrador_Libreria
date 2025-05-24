from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Mapeadores.UsuarioSistemaMapeadores import (
    dto_a_usuario_sistema,
    usuario_sistema_a_dto,
    fila_a_usuario_sistema
)
from Mapeadores.UsuarioMapeadores import (fila_a_usuario_only_rolID)
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.UsuarioSistemaRepositorio import UsuarioSistemaRepositorio
from Cifrados.MD5 import MD5
from Cifrados.AESHMAC import AESHMAC
from Cifrados.JWT import JWT

repositorio = UsuarioSistemaRepositorio()
jwt = JWT()
md5 = MD5()
aeshmac = AESHMAC()

EXITO = 1
YA_EXISTE = 2

class UsuarioSistemaServicio:
     
    def insertarUsuariosistema(self, dto: UsuarioSistemaDTO) -> UsuarioSistemaDTO:
        try:
            # Cifrar contraseña con MD5
            contrasena_cifrada,salt=md5.encrypt(dto.get_contrasena())
            # Cifrar username con AES-GCM + HMAC
            packed_username,username_hmac_value=aeshmac.sellar(dto.get_nombre_usuario())
             # Mapear a la entidad y asignar valores
            entidad = dto_a_usuario_sistema(dto)
            entidad.Set_Salt(salt)
            entidad.Set_Contrasena(contrasena_cifrada)
            entidad.Set_nombre_Usuario_HMAC(username_hmac_value)
            entidad.Set_nombre_usuario(packed_username)
            #Insertar en la tabla usuarios_sistema
            nuevo_id, estado = repositorio.insertarUsuariosistema(entidad)
            if estado != EXITO:
                return None
            entidad.Set_Id(nuevo_id)
            # Mapear de vuelta a DTO y devolverlo
            return usuario_sistema_a_dto(entidad)
        except Exception as ex:
            return None
        
    def obtenerPorUsername(self, dto: UsuarioSistemaDTO) -> UsuarioSistemaDTO:
        try:
            entidad = dto_a_usuario_sistema(dto)
            username_hmac_value = aeshmac.hmac(entidad.Get_nombre_usuario())
            entidad.Set_nombre_Usuario_HMAC(username_hmac_value)
            fila = repositorio.obtenerPorNombreUsuarioHmac(entidad)
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado)
                return dto_resultado
            else:
                return None
        except Exception as ex:
            return None
        
    def obtenerPorUsernameYContrasena(self, dto: UsuarioSistemaDTO) -> Respuesta:
        try:
            entidad = dto_a_usuario_sistema(dto)
            username_hmac_value = aeshmac.hmac(entidad.Get_nombre_usuario())
            entidad.Set_nombre_Usuario_HMAC(username_hmac_value)
            fila = repositorio.obtenerPorNombreUsuarioHmac(entidad)
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                usuario=fila_a_usuario_only_rolID(fila)

                if not md5.verificar(dto.get_contrasena(),entidad_resultado.Get_Salt(),entidad_resultado.Get_Contrasena()):
                    return Respuesta("Error", "contraseña no valida", [])
                
                payload = {
                        "username": entidad.Get_nombre_usuario(),
                        "rol": usuario.Get_RolId()
                    }
                jwt_code = JWT.cifrar(payload)

                return Respuesta("Operación Exitosa", "Usuario Logueado", f"Bienvenido {entidad.Get_nombre_usuario()}", jwt_code)
            else:
                return Respuesta("Error", "Usuario no encontrado", [])
        except Exception as ex:
            return Respuesta("Error", f"Excepción durante validación {ex}", [])

    def listarUsuariosistema(self) -> Respuesta:
        try:
            lista = repositorio.listarUsuariosistema()
            dto_resultado = [usuario_sistema_a_dto(fila_a_usuario_sistema(f)) for f in lista]
            usuarios_desencriptados = []
            for dto in dto_resultado:
                usuario = dto.to_dict_simple()
                usuario["nombreUsuario"] = aeshmac.desellarlo(usuario["nombreUsuario"])
                usuarios_desencriptados.append(usuario)
            if usuarios_desencriptados:
                return Respuesta("Operación Exitosa", "Usuarios del sistema encontrados", usuarios_desencriptados)
            else:
                return Respuesta("Operación Exitosa", "No hay usuarios del sistema registrados", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al listar usuarios del sistema: {ex}", [])

    def obtenerUsuarioSistemaPorId(self, dto: UsuarioSistemaDTO) -> Respuesta:
        try:
            entidad = dto_a_usuario_sistema(dto)
            fila = repositorio.obtenerPorId(entidad)
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado)
                usuario = dto_resultado.to_dict_simple()
                usuario["nombreUsuario"] = aeshmac.desellarlo(usuario["nombreUsuario"])
                return Respuesta("Operación Exitosa", "Usuario del sistema encontrado por ID", usuario)
            else:
                return Respuesta("Error", "No existe el registro", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al obtener usuario del sistema: {ex}", [])

    def obtenerPorUsernameConRespuesta(self, dto: UsuarioSistemaDTO) -> Respuesta:
        try:
            entidad = dto_a_usuario_sistema(dto)
            username_hmac = aeshmac.hmac(entidad.Get_nombre_usuario())
            entidad.Set_nombre_Usuario_HMAC(username_hmac)

            fila = repositorio.obtenerPorNombreUsuarioHmac(entidad)
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado)

                usuario = dto_resultado.to_dict_simple()
                usuario["nombreUsuario"] = aeshmac.desellarlo(usuario["nombreUsuario"])

                return Respuesta("Operación Exitosa", "Encontrado por username", usuario)
            else:
                return Respuesta("Error", "No existe ese username", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar por username: {ex}", [])

    def actualizarUsuarioSistemaPorId(self, dto: UsuarioSistemaDTO) -> Respuesta:
        try:
            # Encriptar valores
            contrasena_cifrada, salt = md5.encrypt(dto.get_contrasena())
            packed_username, username_hmac_value = aeshmac.sellar(dto.get_nombre_usuario())

            entidad = dto_a_usuario_sistema(dto)
            fila = repositorio.obtenerPorId(entidad)
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado)

                 # Mapear entidad
                entidad = dto_a_usuario_sistema(dto)
                entidad.Set_UsuarioId(dto_resultado.get_usuario_id())
                entidad.Set_Salt(salt)
                entidad.Set_Contrasena(contrasena_cifrada)
                entidad.Set_nombre_Usuario_HMAC(username_hmac_value)
                entidad.Set_nombre_usuario(packed_username)

                estado = repositorio.actualizarNombreUsuario(entidad)
                if estado == EXITO:
                    dto_resultado_actualizado=usuario_sistema_a_dto(entidad)
                    usuario = dto_resultado_actualizado.to_dict_simple()
                    usuario["nombreUsuario"] = aeshmac.desellarlo(usuario["nombreUsuario"])
                    return Respuesta("Operación Exitosa", "Actualizado correctamente", usuario)
                else:
                    return Respuesta("Operación Fallida", "No se pudo actualizar el usuario sistema", [])
            else:
                return Respuesta("Error", "No existe el usuario de sistema", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error durante la actualización: {ex}", [])

    def eliminarNombreUsuario(self, dto: UsuarioSistemaDTO) -> Respuesta:
        try:
            entidad = dto_a_usuario_sistema(dto)
            fila = repositorio.obtenerPorId(entidad)
            if not fila:
                return Respuesta("Operación Fallida", "No existe el usuario sistema a eliminar", [])
            estado = repositorio.eliminarNombreUsuario(entidad)
            if estado == EXITO:
                dto_resultado=usuario_sistema_a_dto(fila_a_usuario_sistema(fila))
                usuario = dto_resultado.to_dict_simple()
                usuario["nombreUsuario"] = aeshmac.desellarlo(usuario["nombreUsuario"])
                return Respuesta("Operación Exitosa", "Eliminado correctamente", usuario)
            return Respuesta("Error", "No se pudo eliminar", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error durante la eliminación: {ex}", [])