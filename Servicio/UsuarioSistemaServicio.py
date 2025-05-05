from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Mapeadores.UsuarioSistemaMapeadores import (
    dto_a_usuario_sistema,
    usuario_sistema_a_dto,
    fila_a_usuario_sistema
)
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.UsuarioSistemaRepositorio import UsuarioSistemaRepositorio

from Cifrados.MD5 import MD5
from Cifrados.AESHMAC import AESHMAC
import msgpack
md5=MD5()
aeshmac=AESHMAC()
repositorio = UsuarioSistemaRepositorio()

EXITO = 1
YA_EXISTE = 2

class UsuarioSistemaServicio:

    def insertar(self, dto: UsuarioSistemaDTO) -> Respuesta:
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
                return Respuesta("Operación Exitosa", "UsuarioSistema insertado", [str(dto_resultado)])
            else:
                return Respuesta("Error", "UsuarioSistema no encontrado luego de insertar", [])
        elif estado == YA_EXISTE:
            return Respuesta("Error", "El username ya existe", [])
        return Respuesta("Error", "Error al insertar", [])

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