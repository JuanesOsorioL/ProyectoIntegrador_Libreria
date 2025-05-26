import pyodbc
from Entidades.Venta import Venta
from Utilidades.Configuracion import Configuracion

class VentaRepositorio:

    def insertarVenta(self, venta: Venta) -> tuple:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_insert_venta(?, ?, ?, @p_NuevoId, @p_Respuesta)}"
        cursor.execute(consulta, (
            venta.usuario_id,
            venta.empleado_id,
            venta.total
        ))
        cursor.execute("SELECT @p_NuevoId, @p_Respuesta")
        resultado = cursor.fetchone()
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarTodos(self):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_ventas()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorId(self, id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_venta_por_id(?)}", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def actualizarVenta(self, venta: Venta) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_update_venta(?, ?, ?, ?, ?, @p_Respuesta)}"
        cursor.execute(consulta, (
            venta.id,
            venta.usuario_id,
            venta.empleado_id,
            venta.fecha,
            venta.total
        ))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo

    def borrarVenta(self, id: int) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_venta(?, @p_Respuesta)}", (id,))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo
