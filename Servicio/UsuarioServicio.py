from Cifrados.MD5 import MD5
from Cifrados.JWT import JWT
from Cifrados.AESHMAC import AESHMAC
from Dtos.UsuarioDTO import UsuarioDTO
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Dtos.Generico.Respuesta import Respuesta
from Mapeadores.UsuarioMapeadores import dto_a_usuario,dto_a_usuario_dos,usuario_a_dto,fila_a_usuario,usuario_a_dto_dos
from Repositorios.UsuarioRepositorio import UsuarioRepositorio
from Servicio.UsuarioSistemaServicio import UsuarioSistemaServicio
from Servicio.RolServicio import RolServicio

repositorio = UsuarioRepositorio()
rolServicio=RolServicio()
usuarioSistemaServicio=UsuarioSistemaServicio()
jwt = JWT()
md5 = MD5()
aeshmac = AESHMAC()

EXITO = 1
YA_EXISTE = 2

class UsuarioServicio:

    @staticmethod
    def encapsular(usuario_dto:UsuarioDTO) -> dict:
        nombre_packed,nombre_hmac=aeshmac.sellar(usuario_dto.Get_Nombre())
        email_packed,email_hmac=aeshmac.sellar(usuario_dto.Get_Email())
        telefono_packed,telefono_hmac=aeshmac.sellar(usuario_dto.Get_Telefono())
        direccion_packed,direccion_hmac=aeshmac.sellar(usuario_dto.Get_Direccion())
        
        return  {
            "nombre": nombre_packed,
            "nombre_hmac": nombre_hmac,
            "email": email_packed,
            "email_hmac": email_hmac,
            "telefono": telefono_packed,
            "telefono_hmac": telefono_hmac,
            "direccion": direccion_packed,
            "direccion_hmac": direccion_hmac
        }
    
    def insertarUsuario(self, dto: UsuarioSistemaDTO):
        try:
            
            rolDTO = rolServicio.ExisteRol(dto.get_usuarioDTO().Get_RolDTO())#rol dto completo
            if not rolDTO:
                return Respuesta("Operación Fallida", "El rol no existe", [])

            usuario_dto = dto.get_usuarioDTO()
            datos_encriptados = UsuarioServicio.encapsular(usuario_dto)
            usuario = dto_a_usuario_dos(usuario_dto, datos_encriptados)
            # Validar email
            if repositorio.mostrarUsuarioPorEmail(usuario):
                return Respuesta("Operación Fallida", "Email ya existe, validar", [])

            # Validar username
            if usuarioSistemaServicio.obtenerPorUsername(dto):
                return Respuesta("Operación Fallida", "Nombre usuario ya existe, validar", [])

            # Insertar usuario
            nuevo_id, codigo = repositorio.insertarUsuario(usuario)

            if codigo == YA_EXISTE:
                return Respuesta("Operación Fallida", "El usuario ya existe", [])

            if codigo == EXITO:
                usuario.Set_Id(nuevo_id)
                fila = repositorio.mostrarUsuarioPorId(usuario)
                if fila:
                    decifrar_Nombre_Rol=aeshmac.desellarlo(rolDTO.GetNombre())
                    rolDTO.SetNombre(decifrar_Nombre_Rol)
                    usuarioDTO = usuario_a_dto_dos(fila_a_usuario(fila),rolDTO)#usuariodto full
                    dto.set_usuario_id(nuevo_id)
                    usuarioSistemaDTOCreado = usuarioSistemaServicio.insertarUsuariosistema(dto)

                    if usuarioSistemaDTOCreado is None:
                        return Respuesta("Operación Fallida", "Error al insertar en usuarios_sistema", [])
                    
                    usuarioSistemaDTOCreado.set_usuarioDTO(usuarioDTO)

                    payload = {
                        "username": dto.get_nombre_usuario(),
                        "rol": dto.get_usuarioDTO().Get_RolId()
                    }

                    jwt_code = JWT.cifrar(payload)

                    #Pasa a dict para desellarlo
                    result = usuarioSistemaDTOCreado.to_dict()

                    #Desellamos el nombre de usuario del sistema
                    result["nombreUsuario"] = aeshmac.desellarlo(result["nombreUsuario"])

                    #Desellamos todos los campos del usuarioDTO embebido
                    u = result["usuarioDTO"]
                    for campo in ("nombre", "email", "telefono", "direccion"):
                        u[campo] = aeshmac.desellarlo(u[campo])

                    return Respuesta("Operación Exitosa", "Usuario registrado", result, jwt_code)
                
                return Respuesta("Operación Fallida", "No se pudo registrar el usuario", [])

        except Exception as e:
            return Respuesta("Error", f"Ocurrió una excepción: {str(e)}", [])
        
    def obtenerUsuarioPorId(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            fila = repositorio.mostrarUsuarioPorId(usuario)
            if fila:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                #Desellamos todos los campos del usuarioDTO embebido
                usuario_desencriptado = dto_resultado.to_dict_simple()
                for campo in ("nombre", "email", "telefono", "direccion"):
                    usuario_desencriptado[campo] = aeshmac.desellarlo(usuario_desencriptado[campo])
                return Respuesta("Operación Exitosa", "Usuario encontrado", usuario_desencriptado)
            return Respuesta("Operación Fallida", "No existe usuario con ese ID", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar usuario por ID: {ex}", [])
        
    def listarUsuarios(self) -> Respuesta:
        try:
            lista = repositorio.mostrarTodosLosUsuarios()
            dto_resultado = [usuario_a_dto(fila_a_usuario(f)) for f in lista]
            usuarios_desencriptados = []
            for dto in dto_resultado:
                usuario = dto.to_dict_simple()
                for campo in ("nombre", "email", "telefono", "direccion"):
                    usuario[campo] = aeshmac.desellarlo(usuario[campo])
                usuarios_desencriptados.append(usuario)
            if usuarios_desencriptados:
                return Respuesta("Operación Exitosa", "Usuarios encontrados", usuarios_desencriptados)
            else:
                return Respuesta("Operación Exitosa", "No hay usuarios registrados", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al listar usuarios: {ex}", [])

    def obtenerUsuarioPorEmail(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            email_hmac=aeshmac.hmac(usuario.Get_Email())
            usuario.Set_EmailHmac(email_hmac)
            fila = repositorio.mostrarUsuarioPorEmail(usuario)
            if fila:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))

                # Desencriptamos todos los campos del usuarioDTO embebido
                usuario_desencriptado = dto_resultado.to_dict_simple()
                for campo in ("nombre", "email", "telefono", "direccion"):
                    usuario_desencriptado[campo] = aeshmac.desellarlo(usuario_desencriptado[campo])


                return Respuesta("Operación Exitosa", "Usuario encontrado", usuario_desencriptado)
            return Respuesta("Operación Fallida", "No existe usuario con ese correo", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar usuario por correo: {ex}", [])
            
    def obtenerUsuariosPorRolId(self, dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            lista = repositorio.mostrarUsuarioPorRolId(usuario)
            usuarios_desencriptados = []
            for fila in lista:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                usuario_dict = dto_resultado.to_dict_simple()
                for campo in ("nombre", "email", "telefono", "direccion"):
                    usuario_dict[campo] = aeshmac.desellarlo(usuario_dict[campo])
                usuarios_desencriptados.append(usuario_dict)
            if usuarios_desencriptados:
                return Respuesta("Operación Exitosa", "Usuarios encontrados con el mismo Rol ID", usuarios_desencriptados)
            return Respuesta("Operación Fallida", "No existen usuarios con ese Rol ID", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar usuarios por Rol ID: {ex}", [])

    def actualizarUsuario(self, dto: UsuarioDTO) -> Respuesta:
        try:
            datos_encriptados = UsuarioServicio.encapsular(dto)
            usuario = dto_a_usuario_dos(dto, datos_encriptados)
            codigo = repositorio.actualizarUsuario(usuario)
            if codigo == EXITO:
                dto_resultado = usuario_a_dto(usuario)
                # Desencriptar campos sensibles
                usuario_desencriptado = dto_resultado.to_dict_simple()
                for campo in ("nombre", "email", "telefono", "direccion"):
                    usuario_desencriptado[campo] = aeshmac.desellarlo(usuario_desencriptado[campo])
                return Respuesta("Operación Exitosa", "Usuario actualizado correctamente", usuario_desencriptado)
            else:
                return Respuesta("Operación Fallida", "No se pudo actualizar el usuario", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al actualizar usuario: {ex}", [])

    def borrarUsuario(self,dto: UsuarioDTO) -> Respuesta:
        try:
            usuario = dto_a_usuario(dto)
            fila = repositorio.mostrarUsuarioPorId(usuario)
            if not fila:
                return Respuesta("Operación Fallida", "No existe el usuario a eliminar", [])
            codigo = repositorio.borrarUsuario(usuario)
            if codigo == EXITO:
                dto_resultado = usuario_a_dto(fila_a_usuario(fila))
                #Desellamos todos los campos del usuarioDTO embebido
                usuario_desencriptado = dto_resultado.to_dict_simple()
                for campo in ("nombre", "email", "telefono", "direccion"):
                    usuario_desencriptado[campo] = aeshmac.desellarlo(usuario_desencriptado[campo])
                return Respuesta("Operación Exitosa", "Usuario eliminado", usuario_desencriptado)
            return Respuesta("Operación Fallida", "No se pudo eliminar el usuario", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al eliminar usuario: {ex}", [])