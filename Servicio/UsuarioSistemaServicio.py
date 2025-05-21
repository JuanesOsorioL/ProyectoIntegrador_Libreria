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
                    return Respuesta("Error", "Usuario no encontrado1", [])
                
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






    """
        entidad_resultado_dto=fila_a_usuario_sistema_dto(fila)
    validar_contrasena=md5.verificar(dto.get_contrasena(),entidad_resultado.Get_Salt(),entidad_resultado.Get_Contrasena())
    if validar_contrasena:
        packed=(entidad_resultado.Get_nombre_usuario())
        data = msgpack.unpackb(packed)
        nonce = data["nonce"]
        tag = data["tag"]
        ct = data["ct"]
        desencriptarNombreUsuario=aeshmac.decrypt(ct,nonce,tag)
        

        payload = {
            "sub": desencriptarNombreUsuario,
            "roles": entidad_resultado_dto.get_rol_id()
        }
        jwt_code=jwt.cifrar(payload)
        dto_resultado = usuario_sistema_a_dto(entidad_resultado,desencriptarNombreUsuario)

        respuesta_jwt = msgpack.packb({
            "token": jwt_code,
            "resultado": str(dto_resultado)
        })



        
        return Respuesta("Operación Exitosa", "Encontrado", respuesta_jwt)
    else:
        return Respuesta("Error", "Contraseña invalida", [])
    """




























    """
    def insertar(self, dto: UsuarioSistemaDTO) -> UsuarioSistemaDTO:
        try:
            print("usuario sistema entro",dto.to_dict())
            respuesta=None
            contrasena_cifrada,salt=md5.encrypt(dto.get_contrasena())
            ct,nonce,tag=aeshmac.encrypt(dto.get_nombre_usuario())
            username_hmac_value = aeshmac.hmac(dto.get_nombre_usuario())
            packed = msgpack.packb({
                "nonce": nonce,
                "tag":   tag,
                "ct":    ct
            })

            entidad_usuario_sistema = dto_a_usuario_sistema(dto)
            entidad_usuario_sistema.Set_Salt(salt)
            entidad_usuario_sistema.Set_Contrasena(contrasena_cifrada)
            entidad_usuario_sistema.Set_nombre_Usuario_HMAC(username_hmac_value)
            entidad_usuario_sistema.Set_nombre_usuario(packed)

            nuevo_id, estado = repositorio.insertar(entidad_usuario_sistema)
            print("usuario sistema respueta",nuevo_id, estado )

            if estado == EXITO:
                entidad_usuario_sistema.Set_Id(nuevo_id)
                resultado_usuario_sistemaDTO = usuario_sistema_a_dto(entidad_usuario_sistema)
                respuesta= resultado_usuario_sistemaDTO

            return respuesta
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al registrar usuario: {ex}", [])
    
    
    def obtenerPorUsernameYContrasena(self, dto: UsuarioSistemaDTO) -> Respuesta:
        username_hmac_value = aeshmac.hmac(dto.get_nombre_usuario())
        fila = repositorio.obtenerPorHmac(username_hmac_value)
        if fila:
            entidad_resultado = fila_a_usuario_sistema(fila)
            entidad_resultado_dto=fila_a_usuario_sistema_dto(fila)
            validar_contrasena=md5.verificar(dto.get_contrasena(),entidad_resultado.Get_Salt(),entidad_resultado.Get_Contrasena())
            if validar_contrasena:
                packed=(entidad_resultado.Get_nombre_usuario())
                data = msgpack.unpackb(packed)
                nonce = data["nonce"]
                tag = data["tag"]
                ct = data["ct"]
                desencriptarNombreUsuario=aeshmac.decrypt(ct,nonce,tag)
                

                payload = {
                    "sub": desencriptarNombreUsuario,
                    "roles": entidad_resultado_dto.get_rol_id()
                }
                jwt_code=jwt.cifrar(payload)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado,desencriptarNombreUsuario)

                respuesta_jwt = msgpack.packb({
                    "token": jwt_code,
                    "resultado": str(dto_resultado)
                })



                
                return Respuesta("Operación Exitosa", "Encontrado", respuesta_jwt)
            else:
                return Respuesta("Error", "Contraseña invalida", [])
        else:
            return Respuesta("Error", "Usuario no Existe", [])






    def listar(self) -> Respuesta:
        lista = repositorio.listar()
        dtos = [str(usuario_sistema_a_dto(fila_a_usuario_sistema(f))) for f in lista]
        return Respuesta("Operación Exitosa", "Listado de usuarios_sistema", dtos)

    def obtener_por_id(self, dto: UsuarioSistemaDTO) -> Respuesta:
        entidad = dto_a_usuario_sistema(dto)
        fila = repositorio.obtenerPorId(entidad.Get_Id())
        if fila:
            entidad_resultado = fila_a_usuario_sistema(fila)
            dto_resultado = usuario_sistema_a_dto(entidad_resultado)
            return Respuesta("Operación Exitosa", "Encontrado por ID", [str(dto_resultado)])
        return Respuesta("Error", "No existe el registro", [])

    def obtenerPorUsername(self, dto: UsuarioSistemaDTO) -> Respuesta:
        entidad = dto_a_usuario_sistema(dto)
        fila = repositorio.obtenerPorNombreUsuario(entidad.Get_nombre_Usuario_HMAC())
        if fila:
            entidad_resultado = fila_a_usuario_sistema(fila)
            dto_resultado = usuario_sistema_a_dto(entidad_resultado)
            return Respuesta("Operación Exitosa", "Encontrado por username", [str(dto_resultado)])
        return Respuesta("Error", "No existe ese username", [])

    def actualizar(self, dto: UsuarioSistemaDTO) -> Respuesta:
        entidad = dto_a_usuario_sistema(dto)
        estado = repositorio.actualizar(entidad)
        if estado == EXITO:
            fila = repositorio.obtenerPorId(entidad.Get_Id())
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado)
                return Respuesta("Operación Exitosa", "Actualizado", [str(dto_resultado)])
            else:
                return Respuesta("Error", "No encontrado luego de actualizar", [])
        return Respuesta("Error", "No se pudo actualizar", [])

    def eliminar(self, dto: UsuarioSistemaDTO) -> Respuesta:
        entidad = dto_a_usuario_sistema(dto)
        estado = repositorio.eliminar(entidad.Get_Id())
        if estado == EXITO:
            return Respuesta("Operación Exitosa", "Eliminado correctamente", [])
        return Respuesta("Error", "No se pudo eliminar", [])
    """
    
        










    
    



    """
    antes

        def insertar(self, dto: UsuarioSistemaDTO) -> Respuesta:
        print()
        contrasena_cifrada,salt=md5.encrypt(dto.get_contrasena())
        ct,nonce,tag=aeshmac.encrypt(dto.get_nombre_usuario())
        username_hmac_value = aeshmac.hmac(dto.get_nombre_usuario())
        packed = msgpack.packb({
            "nonce": nonce,
            "tag":   tag,
            "ct":    ct
        })

        entidad = dto_a_usuario_sistema(dto)
        entidad.Set_Salt(salt)
        entidad.Set_Contrasena(contrasena_cifrada)
        entidad.Set_nombre_Usuario_HMAC(username_hmac_value)
        entidad.Set_nombre_usuario(packed)

        nuevo_id, estado = repositorio.insertar(entidad)

        if estado == EXITO:
            fila = repositorio.obtenerPorId(nuevo_id)
            if fila:
                entidad_resultado = fila_a_usuario_sistema(fila)
                dto_resultado = usuario_sistema_a_dto(entidad_resultado)

                return Respuesta("Operación Exitosa", "UsuarioSistema insertado", dto_resultado.to_dict())
            else:
                return Respuesta("Error", "UsuarioSistema no encontrado luego de insertar", [])
        elif estado == YA_EXISTE:
            return Respuesta("Error", "El username ya existe", [])
        return Respuesta("Error", "Error al insertar", [])
    """