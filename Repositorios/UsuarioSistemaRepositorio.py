import pyodbc
from Entidades.UsuarioSistema import UsuarioSistema
from Utilidades.Configuracion import Configuracion

class UsuarioSistemaRepositorio:

    def insertarUsuariosistema(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_insert_usuarios_sistema(?,?,?,?,?, @p_nuevo_id, @p_respuesta)}"
        cursor.execute(consulta, usuario.Get_UsuarioId(), usuario.Get_nombre_usuario(), usuario.Get_nombre_Usuario_HMAC(), usuario.Get_Contrasena(), usuario.Get_Salt())
        cursor.execute("SELECT @p_nuevo_id, @p_respuesta")
        resultado = cursor.fetchone()
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado
    
    def obtenerPorNombreUsuarioHmac(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_usuarios_sistema_por_hmac(?)}", usuario.Get_nombre_Usuario_HMAC())
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado
    
    def listarUsuariosistema(self):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_usuarios_sistema()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado
    
    def obtenerPorId(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_usuarios_sistema_por_id(?)}", usuario.Get_Id())
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def actualizarNombreUsuario(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_update_usuarios_sistema(?, ?, ?, ?, ?, ?, @p_respuesta)}", (
            usuario.Get_Id(), usuario.Get_UsuarioId(), usuario.Get_nombre_usuario(), usuario.Get_nombre_Usuario_HMAC(), usuario.Get_Contrasena(), usuario.Get_Salt()
        ))
        cursor.execute("SELECT @p_respuesta")
        resultado = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado

    def eliminarNombreUsuario(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_usuarios_sistema(?, @p_respuesta)}", usuario.Get_Id())
        cursor.execute("SELECT @p_respuesta")
        resultado = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado