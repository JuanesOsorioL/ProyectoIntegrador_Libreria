from Dtos.RolDTO import RolDTO
from Entidades.Rol import Rol
from Mapeadores.RolMapeadores import dto_a_rol, rol_a_dto,fila_a_rol
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.RolRepositorio import RolRepositorio
from Cifrados.AESHMAC import AESHMAC

repositorio =RolRepositorio();
import msgpack
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





    """
    
    


    def MostrarTodosLosRoles(self) -> Respuesta:
        try:
            listaRolDTO = [];
            lista=repositorio.MostrarTodosLosRoles();

            for roles in lista:
                rol = Rol(
                    id=roles[0],
                    nombre=roles[1]
                )
                listaRolDTO.append(rol_a_dto(rol));
            
            if listaRolDTO:
                 return Respuesta("Operación Exitosa","existen roles guardados",[str(rol) for rol in listaRolDTO])
            else:
                return Respuesta("Operación Exitosa","No existen roles guardados",[])
        except Exception as ex:
            return Respuesta("Error Sistema",f"Error al obtener roles: {str(ex)}",[])
        



    def MostrarTodosLosRolesSeleccionar(self) -> list:
        try:
            lista_rolDTO = [];
            lista=repositorio.MostrarTodosLosRoles();

            for roles in lista:
                rol=fila_a_rol(roles)
                lista_rolDTO.append(rol_a_dto(rol));
            
            return lista_rolDTO
        except Exception as ex:
            return lista_rolDTO



    def MostrarRolPorId(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol = dto_a_rol(rolDTO)
            resultado = repositorio.MostrarRolPorId(rol)
            if resultado:
                rol_encontrado = fila_a_rol(resultado)
                rolDTO=rol_a_dto(rol_encontrado)
                return Respuesta("Operación Exitosa","Rol encontrado",[str(rolDTO)])
            else:
                return Respuesta("Operación Fallida","No existe rol con ese ID",[])
        except Exception as ex:
            return Respuesta("Error Sistema",f"Error al buscar rol: {str(ex)}",[])


    def actualizarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol=dto_a_rol(rolDTO)
            codigo = repositorio.actualizarRol(rol)
            if codigo == EXITO:
                resultado = repositorio.MostrarRolPorId(rol)
                rolActualizado = fila_a_rol(resultado)
                return Respuesta("Operación Exitosa","Rol actualizado correctamente",[str(rol_a_dto(rolActualizado))])
            elif codigo == ROL_EXISTE:
                return Respuesta("Operación Fallida","No se encontró el rol con ese ID",[])
            else:
                return Respuesta("Operación Fallida",f"Código inesperado: {codigo}",[])
        except Exception as ex:
            return Respuesta("Error Sistema",f"Error al actualizar rol: {str(ex)}",[])
        
        
    def borrarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol=dto_a_rol(rolDTO)
            rolExiste = repositorio.MostrarRolPorId(rol)
            if not rolExiste:
                return Respuesta("Operación Fallida","No existe el rol a eliminar",[])
            codigo = repositorio.borrarRol(rol)
            if codigo == EXITO:
                rol = fila_a_rol(rolExiste)
                return Respuesta("Operación Exitosa","El rol se eliminó correctamente",[str(rol_a_dto(rol))])
            elif codigo == ROL_EXISTE:
                return Respuesta("Operación fallida","No se encontró el rol a eliminar",[])
            else:
                return Respuesta("Operación Fallida",f"Código inesperado: {codigo}",[])
        except Exception as ex:
            return Respuesta("Error Sistema",f"Error al eliminar rol: {str(ex)}",[])
    
    
    
    """

       
    