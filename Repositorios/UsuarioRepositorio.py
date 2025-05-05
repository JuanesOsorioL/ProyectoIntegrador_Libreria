import pyodbc;
from Entidades.Usuario import Usuario;
from Utilidades.Configuracion import Configuracion

class UsuarioRepositorio:

    def insertarUsuario(self, usuario: Usuario) -> tuple: 
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_usuario(?,?,?,?,?,?, @p_nuevo_id, @p_respuesta);}"
            cursor.execute(consulta, (usuario.Get_Nombre(), usuario.Get_Email(), usuario.Get_Telefono(), usuario.Get_Direccion(),usuario.Get_FechaRegistro() ,usuario.Get_RolId()))
            cursor.execute("SELECT @p_nuevo_id AS nuevo_id, @p_respuesta AS respuesta;")
            codigo = cursor.fetchone()
            conexion.commit()
            return codigo
        finally:
            cursor.close()
            conexion.close()

    def mostrarTodosLosUsuarios(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta: str = """{CALL proc_select_usuarios(@p_respuesta);}""";
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def mostrarUsuarioPorId(self, usuario: Usuario) -> Usuario:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta: str = """{CALL proc_select_usuario_por_id(?);}""";
            cursor.execute(consulta, usuario.Get_Id())
            resultado = cursor.fetchone();
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarUsuario(self, usuario: Usuario) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_usuario(?,?,?,?,?,?,?, @p_respuesta)}"
            cursor.execute(consulta, (usuario.Get_Id(),usuario.Get_Nombre(), usuario.Get_Email(), usuario.Get_Telefono(), usuario.Get_Direccion(),usuario.Get_FechaRegistro(), usuario.Get_RolId()))
            cursor.execute("SELECT @p_respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()
    
    def borrarUsuario(self, usuario: Usuario) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_usuario(?, @p_respuesta)}"
            cursor.execute(consulta, (usuario.Get_Id()))
            cursor.execute("SELECT @p_respuesta;")
            codigo = cursor.fetchone()[0]
            conexion.commit()
            return codigo
        finally:
            cursor.close()
            conexion.close()

    def mostrarUsuarioPorEmail(self, usuario: Usuario) -> Usuario:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta: str = """{CALL proc_select_usuario_por_email(?);}""";
            cursor.execute(consulta, usuario.Get_Email())
            resultado = cursor.fetchone();
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def mostrarUsuarioPorRolId(self, usuario: Usuario) -> Usuario:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta: str = """{CALL proc_select_usuarios_por_rol(?);}""";
            cursor.execute(consulta, usuario.Get_RolId())
            resultado = cursor.fetchall();
            return resultado
        finally:
            cursor.close()
            conexion.close()