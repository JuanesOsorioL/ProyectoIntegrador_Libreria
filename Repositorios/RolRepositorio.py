import pyodbc;
from Dtos.RolDTO import RolDTO
from Utilidades.Configuracion import Configuracion

class RolRepositorio:
        
    def ListarRoles(self) -> list:
        #try:
            conexion = pyodbc.connect(Configuracion.strConnection);

            consulta: str = """{CALL Libreria.proc_select_rol();}""";
            cursor = conexion.cursor();
            cursor.execute(consulta);
            resultado = cursor.fetchall();
            

        #    lista: list = [];
        #    for rol in cursor:
        #        entidad: Rol = Rol();
        #        entidad.SetId(rol[0]);
        #        entidad.SetDescripcion(rol[1]);
        #        lista.append(entidad);

            cursor.close();
            conexion.close();
            return resultado;

        #    for estado in lista:
        #        print(str(estado.GetId()) + ", " + estado.GetNombre());
        #except Exception as ex:
        #    print(str(ex));
	


    def Guardar(self, rolDTO: RolDTO) -> None:
        #try:
            conexion = pyodbc.connect(Configuracion.strConnection);
            cursor = conexion.cursor();

            consulta: str = "{CALL proc_insert_rol('" + rolDTO.GetDescripcion() + "', @Respuesta);}";
            cursor.execute(consulta);
            cursor.commit();

            consulta = "SELECT @Respuesta;";
            cursor.execute(consulta);
            
            cursor.close();
            conexion.close();
            return cursor.fetchone()[0];
        #except Exception as ex:
        #    print(str(ex));



