import pyodbc;
from Entidades.Rol import Rol
from Utilidades.Configuracion import Configuracion

class RolRepositorio:
        
    def insertarRol(self, rol: Rol) -> tuple:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_rol(?, @p_NuevoId, @p_Respuesta);}"
            cursor.execute(consulta, (rol.GetNombre()))
            cursor.execute("SELECT @p_NuevoId AS nuevo_id, @p_Respuesta AS respuesta;")
            codigo = cursor.fetchone()
            conexion.commit()
            return codigo
        finally:
            cursor.close()
            conexion.close()

    def MostrarTodosLosRoles(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta: str = """{CALL proc_select_rol(@p_Respuesta);}""";
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarRolPorId(self,rol: Rol) -> Rol:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection);
            cursor = conexion.cursor();

            consulta = "{CALL proc_select_rol_por_id(?);}"
            cursor.execute(consulta, rol.GetId())
            resultado = cursor.fetchone();
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarRol(self, rol: Rol) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_rol(?, ?, @Respuesta);}"
            cursor.execute(consulta, (rol.GetId(), rol.GetNombre()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()


    def borrarRol(self, rol: Rol) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_rol(?, @Respuesta);}"
            cursor.execute(consulta, (rol.GetId()))
            cursor.execute("SELECT @Respuesta;")
            codigo = cursor.fetchone()[0]
            conexion.commit()
            return codigo
        finally:
            cursor.close()
            conexion.close()