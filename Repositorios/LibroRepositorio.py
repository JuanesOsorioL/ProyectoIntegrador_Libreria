import pyodbc
from Entidades.Libro import Libro
from Utilidades.Configuracion import Configuracion

class LibroRepositorio:

    def insertarLibro(self, libro: Libro) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_libro(?, ?, ?, ?, ?, ?, ?, ?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (
                libro.titulo,
                libro.isbn,
                libro.descripcion,
                libro.anio_publicacion,
                libro.formato,
                libro.editorial_id,
                libro.precio,
                libro.stock
            ))
            cursor.execute("SELECT @p_NuevoId, @p_Respuesta")
            resultado = cursor.fetchone()
            conexion.commit()
            return resultado
        except pyodbc.Error as e:
            error_msg = str(e).lower()
            if "foreign key constraint fails" in error_msg:
                raise ValueError("La editorial ingresada no existe.")
            raise e

        finally:
            cursor.close()
            conexion.close()


    def mostrarTodos(self):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_libros()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def mostrarPorId(self, id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_libro_por_id(?)}", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def actualizarLibro(self, libro: Libro) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_libro(?, ?, ?, ?, ?, ?, ?, ?, ?, @p_Respuesta)}"
            cursor.execute(consulta, (
                libro.id,
                libro.titulo,
                libro.isbn,
                libro.descripcion,
                libro.anio_publicacion,
                libro.formato,
                libro.editorial_id,
                libro.precio,
                libro.stock
            ))
            cursor.execute("SELECT @p_Respuesta")
            codigo = cursor.fetchone()[0]
            conexion.commit()
            return codigo
        except pyodbc.Error as e:
            error_msg = str(e).lower()
            if "foreign key constraint fails" in error_msg:
                raise ValueError("La editorial ingresada no existe.")
            raise e
        finally:
            cursor.close()
            conexion.close()

    def borrarLibro(self, id: int) -> int:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_libro(?, @p_Respuesta)}", (id,))
        cursor.execute("SELECT @p_Respuesta")
        codigo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return codigo
