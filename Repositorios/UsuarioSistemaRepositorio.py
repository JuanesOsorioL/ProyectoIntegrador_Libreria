import pyodbc
from Entidades.UsuarioSistema import UsuarioSistema
from Utilidades.Configuracion import Configuracion

class UsuarioSistemaRepositorio:

    def insertar(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        consulta = "{CALL proc_insert_usuarios_sistema(?, ?, ?, @p_nuevo_id, @p_respuesta)}"
        cursor.execute(consulta, usuario.Get_UsuarioId(), usuario.Get_Username(), usuario.Get_PasswordHash())
        cursor.execute("SELECT @p_nuevo_id, @p_respuesta")
        resultado = cursor.fetchone()
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado

    def listar(self):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_usuarios_sistema()}")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def obtener_por_id(self, id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_usuarios_sistema_por_id(?)}", id)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def obtener_por_username(self, username: str):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_select_usuarios_sistema_por_username(?)}", username)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    def actualizar(self, usuario: UsuarioSistema):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_update_usuarios_sistema(?, ?, ?, ?, @p_respuesta)}", (
            usuario.Get_Id(), usuario.Get_UsuarioId(), usuario.Get_Username(), usuario.Get_PasswordHash()
        ))
        cursor.execute("SELECT @p_respuesta")
        resultado = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado

    def eliminar(self, id: int):
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()
        cursor.execute("{CALL proc_delete_usuarios_sistema(?, @p_respuesta)}", id)
        cursor.execute("SELECT @p_respuesta")
        resultado = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return resultado