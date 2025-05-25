import pyodbc
from Entidades.LibroAutor import LibroAutor
from Utilidades.Configuracion import Configuracion

class LibroAutorRepositorio:

    def insertarLibroAutor(self, libro_autor: LibroAutor) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_libro_autor(?, ?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (libro_autor.GetIdLibro(), libro_autor.GetIdAutor()))
            cursor.execute("SELECT @p_NuevoId AS nuevo_id, @p_Respuesta AS respuesta;")
            resultado = cursor.fetchone()
            conexion.commit()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def mostrarTodosLosLibroAutor(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_libro_autor()}"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def mostrarLibroAutorPorId(self, libro_autor: LibroAutor) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_libro_autor_por_id(?)}"
            cursor.execute(consulta, libro_autor.GetId())
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarLibroAutor(self, libro_autor: LibroAutor) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_libro_autor(?, ?, ?, @Respuesta)}"
            cursor.execute(consulta, (libro_autor.GetId(), libro_autor.GetIdLibro(), libro_autor.GetIdAutor()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()

    def borrarLibroAutor(self, libro_autor: LibroAutor) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_libro_autor(?, @Respuesta)}"
            cursor.execute(consulta, libro_autor.GetId())
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()
