import pyodbc;
from Dtos.RolDTO import RolDTO
from Utilidades.Configuracion import Configuracion

class RolRepositorio:
        
    def insertarRol(self, rolDTO: RolDTO) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_insert_rol(?, @p_NuevoId, @p_Respuesta)}"
            cursor.execute(consulta, (rolDTO.GetNombre()))
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
            consulta: str = """{CALL proc_select_rol();}""";
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def MostrarRolPorId(self,rolDTO: RolDTO) -> RolDTO:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection);
            cursor = conexion.cursor();

            consulta = "{CALL proc_select_rol_por_id(?)}"
            cursor.execute(consulta, rolDTO.GetId())
            resultado = cursor.fetchone();
            return resultado
        finally:
            cursor.close()
            conexion.close()

    def actualizarRol(self, rolDTO: RolDTO) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_update_rol(?, ?, @Respuesta)}"
            cursor.execute(consulta, (rolDTO.GetId(), rolDTO.GetNombre()))
            cursor.execute("SELECT @Respuesta;")
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
        finally:
            cursor.close()
            conexion.close()


    def borrarRol(self, rolDTO: RolDTO) -> int:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "{CALL proc_delete_rol(?, @Respuesta)}"
            cursor.execute(consulta, (rolDTO.GetId()))
            cursor.execute("SELECT @Respuesta;")
            codigo = cursor.fetchone()[0]
            conexion.commit()
            return codigo
        finally:
            cursor.close()
            conexion.close()