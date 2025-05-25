import pyodbc
from Entidades.LibroCategoria import LibroCategoria
from Utilidades.Configuracion import Configuracion

class LibroCategoriaRepositorio:

    def insertarLibroCategoria(self, libro_categoria: LibroCategoria) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_libro_categoria(?, ?, @p_Respuesta)}"
            cursor.execute(consulta, (libro_categoria.GetLibroId(), libro_categoria.GetCategoriaId()))
            cursor.execute("SELECT @p_Respuesta AS respuesta;")
            resultado = cursor.fetchone()
            conexion.commit()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def mostrarTodosLosLibroCategoria(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_libro_categoria()}"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def mostrarLibroCategoriaPorId(self, libro_categoria: LibroCategoria) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_select_libro_categoria_por_id(?, ?)}"
            cursor.execute(consulta, (libro_categoria.GetLibroId(), libro_categoria.GetCategoriaId()))
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarLibroCategoria(self, libro_categoria: LibroCategoria, nuevo_libro_id: int, nueva_categoria_id: int) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_libro_categoria(?, ?, ?, ?, @Respuesta)}"
            cursor.execute(consulta, (
                libro_categoria.GetLibroId(), 
                libro_categoria.GetCategoriaId(), 
                nuevo_libro_id, 
                nueva_categoria_id
            ))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()

    def borrarLibroCategoria(self, libro_categoria: LibroCategoria) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_libro_categoria(?, ?, @Respuesta)}"
            cursor.execute(consulta, (libro_categoria.GetLibroId(), libro_categoria.GetCategoriaId()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()
