import pyodbc
from Entidades.Editorial import Editorial
from Utilidades.Configuracion import Configuracion

class EditorialRepositorio:

    def insertarEditorial(self, editorial: Editorial) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_editorial(?, ?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (editorial.GetNombre(), editorial.GetPais()))
            cursor.execute("SELECT @p_NuevoId AS nuevo_id, @p_Respuesta AS respuesta;")
            resultado = cursor.fetchone()
            conexion.commit()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarTodasLasEditoriales(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_editorial()}"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarEditorialPorId(self, editorial: Editorial) -> Editorial:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_editorial_por_id(?)}"
            cursor.execute(consulta, editorial.GetId())
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarEditorial(self, editorial: Editorial) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_editorial(?, ?, ?, @Respuesta)}"
            cursor.execute(consulta, (editorial.GetId(), editorial.GetNombre(), editorial.GetPais()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()

    def borrarEditorial(self, editorial: Editorial) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_editorial(?, @Respuesta)}"
            cursor.execute(consulta, editorial.GetId())
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()
