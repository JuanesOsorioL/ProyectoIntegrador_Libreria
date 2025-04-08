import pyodbc;
from Entidades import Rol;
from Utilidades import Configuracion

class repositorio:

    def GuardarRol(self, rol: Rol) -> bool:
        conexion = pyodbc.connect(Configuracion.Configuracion());
        cursor = conexion.cursor();

        cursor.execute("INSERT INTO cuentas (idTipo,idPersona,saldoInicial) VALUES (?,?,?);", ())

        cursor.execute("SELECT LAST_INSERT_ID();")
        id_generado  = cursor.fetchone()[0];

        cursor.commit();

        cursor.execute("SELECT * FROM cuentas WHERE id = ?;", (id_generado,))
        fila = cursor.fetchone() 

        cursor.close();
        conexion.close();
        return fila;