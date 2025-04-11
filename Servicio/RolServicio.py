from Dtos.RolDTO import RolDTO
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.RolRepositorio import RolRepositorio

repositorio =RolRepositorio();

class RolServicio:
       
    def insertarRol(self, rolDTO: RolDTO) -> Respuesta:
        try:
            resultado=repositorio.insertarRol(rolDTO);
            codigo=resultado[1]
            if codigo==1:
                newRolDTO = RolDTO(id=resultado[0], nombre="")
                resultadoRolDTO = repositorio.MostrarRolPorId(newRolDTO)
                return Respuesta(
                    estado="Operación exitosa",
                    msj="Se guardo el nuevo Rol",
                    resultado=[str(resultadoRolDTO)]
                )
            elif codigo==2:
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
            lista: list = [];
            listaRolDTO: list[RolDTO] = [];
            lista=repositorio.MostrarTodosLosRoles();

            for roles in lista:
                newRolDTO = RolDTO(
                    id=roles[0],
                    nombre=roles[1]
                )
                listaRolDTO.append(newRolDTO);
            
            if listaRolDTO:
                 return Respuesta(
                    estado="Operación exitosa",
                    msj="existen roles guardados",
                    resultado=[str(rol) for rol in listaRolDTO]
                )
            else:
                return Respuesta(
                    estado="Operación fallida",
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
            resultado: RolDTO = repositorio.MostrarRolPorId(rolDTO)
            if resultado:
                rolEncontrado = RolDTO(id=resultado[0], nombre=resultado[1])
                return Respuesta(
                    estado="Operación exitosa",
                    msj="Rol encontrado",
                    resultado=[str(rolEncontrado)]
                )
            else:
                return Respuesta(
                    estado="Operación fallida",
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
            codigo = repositorio.actualizarRol(rolDTO)
            print(codigo)
            if codigo == 1:
                return Respuesta(
                    estado="Operación exitosa",
                    msj="Rol actualizado correctamente",
                    resultado=[str(rolDTO.GetNombre())]
                )
            elif codigo == 2:
                return Respuesta(
                    estado="Operación fallida",
                    msj="No se encontró el rol con ese ID",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación fallida",
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
            codigo = repositorio.borrarRol(rolDTO)
            if codigo == 1:
                return Respuesta(
                    estado="Operación exitosa",
                    msj="El rol se eliminó correctamente",
                    resultado=[str(rolDTO.GetNombre())]
                )
            elif codigo == 2:
                return Respuesta(
                    estado="Operación fallida",
                    msj="No se encontró el rol a eliminar",
                    resultado=[]
                )
            else:
                return Respuesta(
                    estado="Operación fallida",
                    msj=f"Código inesperado: {codigo}",
                    resultado=[]
                )
        except Exception as ex:
            return Respuesta(
                estado="Error Sistema",
                msj=f"Error al eliminar rol: {str(ex)}",
                resultado=[]
            )