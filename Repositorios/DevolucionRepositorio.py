import pyodbc
from Entidades.Devolucion import Devolucion
from Utilidades.Configuracion import Configuracion


class DevolucionRepositorio:

    def insertarDevolucion(self, devolucion: Devolucion) -> tuple:
        try:
            print(devolucion.to_dict_simple())
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "{CALL proc_insert_devolucion(?, ?, ? ,?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (
                devolucion.GetFechaRealDevolucion(),
                devolucion.GetPrestamoId(),
                devolucion.GetEstadoLibro(),
                devolucion.GetObservaciones()
            ))
            cursor.execute("SELECT @p_NuevoId AS nuevo_id, @p_Respuesta AS respuesta;")
            resultado = cursor.fetchone()
            conexion.commit()
            print(resultado)
            if resultado:
                nuevo_id = resultado.nuevo_id
                codigo = resultado.respuesta
                return (nuevo_id, codigo)
            else:
                return (None, -1)
        finally:
            cursor.close()
            conexion.close()

    def MostrarTodasLasDevoluciones(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("{CALL proc_select_devolucion()}")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()

    def MostrarDevolucionPorId(self, devolucion: Devolucion) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("{CALL proc_select_devolucion_por_id(?)}", (devolucion.GetId(),))
            return cursor.fetchone()
        finally:
            cursor.close()
            conexion.close()

    def actualizarDevolucion(self, devolucion: Devolucion) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_devolucion(?,?, ?, ?, ?, @Respuesta)}"
            cursor.execute(consulta, (
                devolucion.GetId(),
                devolucion.GetPrestamoId(),
                devolucion.GetFechaRealDevolucion(),
                devolucion.GetEstadoLibro(),
                devolucion.GetObservaciones()
            ))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()

    def borrarDevolucion(self, devolucion: Devolucion) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("{CALL proc_delete_devolucion(?, @Respuesta)}", (devolucion.GetId(),))
            cursor.execute("SELECT @Respuesta;")
            codigo = cursor.fetchone()[0]
            conexion.commit()
            return codigo
        finally:
            cursor.close()
            conexion.close()
