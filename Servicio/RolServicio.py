from Dtos.RolDTO import RolDTO
from Entidades.Rol import Rol
from Mapeadores.Mapeadores import dto_a_rol, rol_a_dto,fila_a_rol
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
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Se guardo el nuevo Rol",
                    resultado=[str(rol_a_dto(rol_encontrado))]
                )
            elif codigo==ROL_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="Rol ya Existe",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se realizo el guardado",
                    resultado=[]
                )

        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error en la inserción: {ex}",
                resultado=[]
            )

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
                 return Respuesta(
                    estado="Operación Exitosa",
                    msj="existen roles guardados",
                    resultado=[str(rol) for rol in listaRolDTO]
                )
            else:
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="No existen roles guardados",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al obtener roles: {str(ex)}",
                resultado=[]
            )

    def MostrarRolPorId(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol = dto_a_rol(rolDTO)
            resultado = repositorio.MostrarRolPorId(rol)
            if resultado:
                rol_encontrado = fila_a_rol(resultado)
                rolDTO=rol_a_dto(rol_encontrado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Rol encontrado",
                    resultado=[str(rolDTO)]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe rol con ese ID",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al buscar rol: {str(ex)}",
                resultado=[]
            )

    def actualizarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol=dto_a_rol(rolDTO)
            codigo = repositorio.actualizarRol(rol)
            if codigo == EXITO:
                resultado = repositorio.MostrarRolPorId(rol)
                rolActualizado = fila_a_rol(resultado)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="Rol actualizado correctamente",
                    resultado=[str(rol_a_dto(rolActualizado))]
                )
            elif codigo == ROL_EXISTE:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No se encontró el rol con ese ID",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj=f"Código inesperado: {codigo}",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
               estado="Error Sistema",
                msj=f"Error al actualizar rol: {str(ex)}",
                resultado=[]
            )
        
    def borrarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            rol=dto_a_rol(rolDTO)
            rolExiste = repositorio.MostrarRolPorId(rol)
            if not rolExiste:
                return Respuesta(
                    estado="Operación Fallida",
                    msj="No existe el rol a eliminar",
                    resultado=[]
                )
            codigo = repositorio.borrarRol(rol)
            if codigo == EXITO:
                rol = fila_a_rol(rolExiste)
                return Respuesta(
                    estado="Operación Exitosa",
                    msj="El rol se eliminó correctamente",
                    resultado=[str(rol_a_dto(rol))]
                )
            elif codigo == ROL_EXISTE:
                return Respuesta(
                    estado="Operación fallida",
                    msj="No se encontró el rol a eliminar",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación Fallida",
                    msj=f"Código inesperado: {codigo}",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al eliminar rol: {str(ex)}",
                resultado=[]
            )