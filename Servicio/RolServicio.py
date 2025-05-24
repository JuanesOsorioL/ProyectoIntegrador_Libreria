from Dtos.RolDTO import RolDTO
from Mapeadores.Mapeadores import dto_a_rol, rol_a_dto,fila_a_rol
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.RolRepositorio import RolRepositorio
from Cifrados.AESHMAC import AESHMAC

repositorio =RolRepositorio()
aeshmac=AESHMAC()

EXITO = 1
ROL_EXISTE = 2

class RolServicio:
  
    def ExisteRol(self, rolDTO: RolDTO) -> RolDTO:
        try:
            rol = dto_a_rol(rolDTO)
            resultado = repositorio.MostrarRolPorId(rol)
            if resultado:
                rol_encontrado = fila_a_rol(resultado)
                rolDTO=rol_a_dto(rol_encontrado)
                return rolDTO
            else:
                return None
        except Exception as ex:
            return None

    def insertarRol(rolDTO: RolDTO) -> Respuesta:
        try:
            rol=dto_a_rol(rolDTO)
            packed, hmac_val = aeshmac.sellar(rol.GetNombre())
            rol.SetNombre(packed)
            rol.SetNombreHmac(hmac_val)
            resultado=repositorio.insertarRol(rol)
            nuevo_id, codigo = resultado
            if codigo==EXITO:
                rol.SetId(nuevo_id)
                nombre_desencriptado=aeshmac.desellarlo(rol.GetNombre())
                rol.SetNombre(nombre_desencriptado)
                return Respuesta("Operación Exitosa","Se guardo el nuevo Rol",rol_a_dto(rol).to_dict())
            elif codigo==ROL_EXISTE:
                return Respuesta("Operación Fallida","Rol ya Existe",[])
            else:
                return Respuesta("Operación Fallida","No se realizo el guardado",[])

        except Exception as ex:
            return Respuesta("Error Sistema",f"Error en la inserción: {ex}",[])

    def MostrarTodosLosRoles(self) -> Respuesta:
        try:
            lista_roles = []
            filas = repositorio.MostrarTodosLosRoles()
            for fila in filas:
                rol = fila_a_rol(fila)
                rol.SetNombre(aeshmac.desellarlo(rol.GetNombre()))
                lista_roles.append(rol_a_dto(rol))
            return Respuesta("Operación Exitosa", "Existen roles guardados", [r.to_dict() for r in lista_roles])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al obtener roles: {str(ex)}", [])

    def MostrarRolPorId(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol = dto_a_rol(rolDTO)
            fila = repositorio.MostrarRolPorId(rol)
            if fila:
                rol = fila_a_rol(fila)
                rol.SetNombre(aeshmac.desellarlo(rol.GetNombre()))
                return Respuesta("Operación Exitosa", "Rol encontrado", [rol_a_dto(rol).to_dict()])
            return Respuesta("Operación Fallida", "No existe rol con ese ID", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al buscar rol: {str(ex)}", [])

    def actualizarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            # Verificar si el rol existe
            rol = dto_a_rol(rolDTO)
            fila_existente = repositorio.MostrarRolPorId(rol)
            if not fila_existente:
                return Respuesta("Operación Fallida", "No se encontró el rol con ese ID", [])
            # Si existe, proceder a actualizar
            packed, hmac_val = aeshmac.sellar(rol.GetNombre())
            rol.SetNombre(packed)
            rol.SetNombreHmac(hmac_val)
            codigo = repositorio.actualizarRol(rol)
            if codigo == EXITO:
                rol.SetNombre(aeshmac.desellarlo(rol.GetNombre()))
                return Respuesta("Operación Exitosa", "Rol actualizado correctamente", [rol_a_dto(rol).to_dict()])
            else:
                return Respuesta("Operación Fallida", "No se pudo actualizar el rol", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al actualizar rol: {str(ex)}", [])

    def borrarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol = dto_a_rol(rolDTO)
            fila = repositorio.MostrarRolPorId(rol)
            if not fila:
                return Respuesta("Operación Fallida", "No existe el rol a eliminar", [])
            codigo = repositorio.borrarRol(rol)
            if codigo == EXITO:
                rol = fila_a_rol(fila)
                rol.SetNombre(aeshmac.desellarlo(rol.GetNombre()))
                return Respuesta("Operación Exitosa", "El rol se eliminó correctamente", [rol_a_dto(rol).to_dict()])
            return Respuesta("Operación Fallida", "Error al eliminar el rol", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error al eliminar rol: {str(ex)}", [])

    def insertarNuevoRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol = dto_a_rol(rolDTO)
            packed, hmac_val = aeshmac.sellar(rol.GetNombre())
            rol.SetNombre(packed)
            rol.SetNombreHmac(hmac_val)
            nuevo_id, codigo = repositorio.insertarRol(rol)
            if codigo == EXITO:
                rol.SetId(nuevo_id)
                rol.SetNombre(aeshmac.desellarlo(rol.GetNombre()))
                return Respuesta("Operación Exitosa", "Se guardó el nuevo Rol", rol_a_dto(rol).to_dict())
            elif codigo == ROL_EXISTE:
                return Respuesta("Operación Fallida", "Rol ya existe", [])
            return Respuesta("Operación Fallida", "No se realizó el guardado", [])
        except Exception as ex:
            return Respuesta("Error Sistema", f"Error en la inserción: {ex}", [])