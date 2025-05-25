import pyodbc
from Entidades.Categoria import Categoria
from Utilidades.Configuracion import Configuracion

class CategoriaRepositorio:

    def insertarCategoria(self, categoria: Categoria) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_categoria(?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (categoria.GetNombre(),))
            cursor.execute("SELECT @p_NuevoId AS nuevo_id, @p_Respuesta AS respuesta;")
            resultado = cursor.fetchone()
            conexion.commit()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarTodasLasCategorias(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_categoria()}"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarCategoriaPorId(self, categoria: Categoria) -> Categoria:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_categoria_por_id(?)}"
            cursor.execute(consulta, categoria.GetId())
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarCategoria(self, categoria: Categoria) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_categoria(?, ?, @Respuesta)}"
            cursor.execute(consulta, (categoria.GetId(), categoria.GetNombre()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()

    def borrarCategoria(self, categoria: Categoria) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_categoria(?, @Respuesta)}"
            cursor.execute(consulta, categoria.GetId())
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()
