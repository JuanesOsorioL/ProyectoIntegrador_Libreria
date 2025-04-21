from Dtos.DevolucionDTO import DevolucionDTO
from Entidades.Devolucion import Devolucion
from Mapeadores.Mapeadores import dto_a_devolucion, devolucion_a_dto, fila_a_devolucion
from Dtos.Generico.Respuesta import Respuesta
from Repositorios.DevolucionRepositorio import DevolucionRepositorio

repositorio = DevolucionRepositorio()

EXITO = 1
YA_EXISTE = 2

class DevolucionServicio:

    def insertarDevolucion(self, dto: DevolucionDTO) -> Respuesta:
        try:
            devolucion = dto_a_devolucion(dto)
            nuevo_id, codigo = repositorio.insertarDevolucion(devolucion)
            if codigo == EXITO:
                dev_tmp = Devolucion(nuevo_id,None,None,None)
                fila = repositorio.MostrarDevolucionPorId(dev_tmp)
                dev = fila_a_devolucion(fila)
                return Respuesta("Operación Exitosa", "Se guardó la devolución", [str(devolucion_a_dto(dev))])
            elif codigo == YA_EXISTE:
                return Respuesta("Operación Fallida", "La devolución ya existe", [])
            else:
                return Respuesta("Operación Fallida", "Error desconocido", [])
        except Exception as e:
            return Respuesta("Error Sistema", f"Error al insertar devolución: {str(e)}", [])

    def MostrarTodasLasDevoluciones(self) -> Respuesta:
        try:
            filas = repositorio.MostrarTodasLasDevoluciones()
            listaDTO = [devolucion_a_dto(fila_a_devolucion(f)) for f in filas]
            if listaDTO:
                return Respuesta("Operación Exitosa", "Lista de devoluciones", [str(d) for d in listaDTO])
            else:
                return Respuesta("Operación Exitosa", "No hay devoluciones registradas", [])
        except Exception as e:
            return Respuesta("Error Sistema", f"Error al obtener devoluciones: {str(e)}", [])

    def MostrarDevolucionPorId(self, dto: DevolucionDTO) -> Respuesta:
        try:
            devolucion = dto_a_devolucion(dto)
            fila = repositorio.MostrarDevolucionPorId(devolucion)
            if fila:
                dto_final = devolucion_a_dto(fila_a_devolucion(fila))
                return Respuesta("Operación Exitosa", "Devolución encontrada", [str(dto_final)])
            else:
                return Respuesta("Operación Fallida", "No existe devolución con ese ID", [])
        except Exception as e:
            return Respuesta("Error Sistema", f"Error al buscar devolución: {str(e)}", [])

    def actualizarDevolucion(self, dto: DevolucionDTO) -> Respuesta:
        try:
            devolucion = dto_a_devolucion(dto)
            codigo = repositorio.actualizarDevolucion(devolucion)
            if codigo == EXITO:
                fila = repositorio.MostrarDevolucionPorId(devolucion)
                dev_actualizada = fila_a_devolucion(fila)
                return Respuesta("Operación Exitosa", "Actualización exitosa", [str(devolucion_a_dto(dev_actualizada))])
            else:
                return Respuesta("Operación Fallida", "No se encontró la devolución a actualizar", [])
        except Exception as e:
            return Respuesta("Error Sistema", f"Error al actualizar: {str(e)}", [])

    def borrarDevolucion(self, dto: DevolucionDTO) -> Respuesta:
        try:
            devolucion = dto_a_devolucion(dto)
            fila = repositorio.MostrarDevolucionPorId(devolucion)
            if not fila:
                return Respuesta("Operación Fallida", "No existe devolución a eliminar", [])
            codigo = repositorio.borrarDevolucion(devolucion)
            if codigo == EXITO:
                dev_eliminada = fila_a_devolucion(fila)
                return Respuesta("Operación Exitosa", "Devolución eliminada", [str(devolucion_a_dto(dev_eliminada))])
            else:
                return Respuesta("Operación Fallida", "No se pudo eliminar la devolución", [])
        except Exception as e:
            return Respuesta("Error Sistema", f"Error al eliminar: {str(e)}", [])
