import pyodbc
from Entidades.DetallePrestamo import DetallePrestamo
from Utilidades.Configuracion import Configuracion

class DetallePrestamoRepositorio:

    def insertarDetalle(self, detalle: DetallePrestamo) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_insert_detalle_prestamo(?, ?, ?, @p_Respuesta)}",
                       (detalle.prestamo_id, detalle.libro_id, detalle.cantidad))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo

    def mostrarTodos(self):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_detalles_prestamo()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorId(self, prestamo_id: int, libro_id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_detalle_prestamo_por_id(?, ?)}", (prestamo_id, libro_id))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorPrestamo(self, prestamo_id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_detalles_por_prestamo(?)}", (prestamo_id,))
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def actualizarDetalle(self, detalle: DetallePrestamo) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_update_detalle_prestamo(?, ?, ?, @p_Respuesta)}",
                       (detalle.prestamo_id, detalle.libro_id, detalle.cantidad))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo

    def borrarDetalle(self, prestamo_id: int, libro_id: int) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_detalle_prestamo(?, ?, @p_Respuesta)}", (prestamo_id, libro_id))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo
