import pyodbc;
from Entidades import Rol;

class repositorio:

    def GuardarRol(self, rol: Rol) -> bool:
    
    try:
        conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
        
        # Llamada al procedimiento almacenado para insertar
        consulta: str = """{CALL proc_insert_rol(?, ?, ?, ?)}"""
        cursor = conexion.cursor()
        
        # Parámetros del procedimiento almacenado (deben coincidir con la definición en la BD)
        params = (
            rol.GetNombre(),
            rol.GetDescripcion(),
            rol.GetPuedePrestar(),
            rol.GetMaxLibros()
        )
        
        cursor.execute(consulta, params)
        conexion.commit()  # Importante para confirmar la transacción
        
        # Obtener el ID generado si es necesario
        if hasattr(rol, 'SetId'):
            cursor.execute("SELECT SCOPE_IDENTITY()")
            id_generado = cursor.fetchone()[0]
            rol.SetId(id_generado)
        
        cursor.close()
        conexion.close()
        
        return True
        
    except Exception as ex:
        print(f"Error al guardar rol: {str(ex)}")
        if 'conexion' in locals():
            conexion.rollback()  # Revertir cambios en caso de error
        return False