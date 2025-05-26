import pyodbc
from Entidades.DetalleVenta import DetalleVenta
from Utilidades.Configuracion import Configuracion

class DetalleVentaRepositorio:

    def insertarDetalle(self, detalle: DetalleVenta) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_insert_detalle_venta(?, ?, ?, ?, ?, @p_Respuesta)}"
        cursor.execute(consulta, (
            detalle.venta_id,
            detalle.libro_id,
            detalle.cantidad,
            detalle.precio_unitario,
            detalle.subtotal
        ))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo

    def mostrarTodos(self):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_detalles_venta()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorId(self, venta_id: int, libro_id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_detalle_por_id(?, ?)}", (venta_id, libro_id))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorVenta(self, venta_id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_detalles_por_venta(?)}", (venta_id,))
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def actualizarDetalle(self, detalle: DetalleVenta) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_update_detalle_venta(?, ?, ?, ?, ?, @p_Respuesta)}"
        cursor.execute(consulta, (
            detalle.venta_id,
            detalle.libro_id,
            detalle.cantidad,
            detalle.precio_unitario,
            detalle.subtotal
        ))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo

    def borrarDetalle(self, venta_id: int, libro_id: int) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_detalle_venta(?, ?, @p_Respuesta)}", (venta_id, libro_id))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo