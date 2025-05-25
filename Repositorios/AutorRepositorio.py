import pyodbc
from Entidades.Autor import Autor
from Utilidades.Configuracion import Configuracion

class AutorRepositorio:

    def insertarAutor(self, autor: Autor) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_autor(?, ?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (autor.GetNombre(), autor.GetNacionalidad()))
            cursor.execute("SELECT @p_NuevoId AS nuevo_id, @p_Respuesta AS respuesta;")
            resultado = cursor.fetchone()
            conexion.commit()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarTodosLosAutores(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_autor()}"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarAutorPorId(self, autor: Autor) -> Autor:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_autor_por_id(?)}"
            cursor.execute(consulta, autor.GetId())
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarAutor(self, autor: Autor) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_autor(?, ?, ?, @Respuesta)}"
            cursor.execute(consulta, (autor.GetId(), autor.GetNombre(), autor.GetNacionalidad()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()

    def borrarAutor(self, autor: Autor) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_autor(?, @Respuesta)}"
            cursor.execute(consulta, autor.GetId())
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()
