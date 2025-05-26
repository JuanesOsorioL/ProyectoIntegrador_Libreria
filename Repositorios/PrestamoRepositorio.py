import pyodbc
from Entidades.Prestamo import Prestamo
from Utilidades.Configuracion import Configuracion

class PrestamoRepositorio:

    def insertarPrestamo(self, prestamo: Prestamo) -> tuple:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_insert_prestamo(?, ?, ?, ?, ?, @p_NuevoId, @p_Respuesta)}"
        cursor.execute(consulta, (
            prestamo.usuario_id,
            prestamo.empleado_id,
            prestamo.fecha_prestamo,
            prestamo.fecha_devolucion,
            prestamo.estado
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
        cursor.execute("{CALL proc_select_prestamos()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorId(self, id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_prestamo_por_id(?)}", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def actualizarPrestamo(self, prestamo: Prestamo) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_update_prestamo(?, ?, ?, ?, ?, ?, @p_Respuesta)}"
        cursor.execute(consulta, (
            prestamo.id,
            prestamo.usuario_id,
            prestamo.empleado_id,
            prestamo.fecha_prestamo,
            prestamo.fecha_devolucion,
            prestamo.estado
        ))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo

    def borrarPrestamo(self, id: int) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_prestamo(?, @p_Respuesta)}", (id,))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo