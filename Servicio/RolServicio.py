from Dtos.RolDTO import RolDTO
from Entidades.Rol import Rol
from Mapeadores.RolMapeadores import dto_a_rol, rol_a_dto,fila_a_rol
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.RolRepositorio import RolRepositorio

repositorio =RolRepositorio();

EXITO = 1
ROL_EXISTE = 2

class RolServicio:
       
    def insertarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol=dto_a_rol(rolDTO)
            resultado=repositorio.insertarRol(rol);
            nuevo_id, codigo = resultado
            if codigo==EXITO:
                nuevoRol = Rol(id=nuevo_id, nombre="")
                resultadoRol = repositorio.MostrarRolPorId(nuevoRol)
                rol_encontrado = fila_a_rol(resultadoRol)
                return Respuesta("Operación Exitosa","Se guardo el nuevo Rol",[str(rol_a_dto(rol_encontrado))]
                )
            elif codigo==ROL_EXISTE:
                return Respuesta("Operación Fallida","Rol ya Existe",[])
            else:
                return Respuesta("Operación Fallida","No se realizo el guardado",[])

        except Exception as ex:
            return Respuesta("Error Sistema",f"Error en la inserción: {ex}",[])


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