from Controlador.RolControlador import RolControlador
import pyodbc;
from Utilidades.Configuracion import Configuracion

rolControlador:RolControlador=RolControlador();

class Menu:

    def mostrar_menu(self):

        while True:
            
            print("\nMenú de Opciones:")
            print("0. Creacion de tablas")
            print("1. Ingresar Rol")
            print("2. Mostrar Los Roles")
            print("3. Mostrar Rol por ID")
            print("4. Actualizar Rol por ID")
            print("5. Borrar Rol por ID")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                Menu.crear_tabla()

            elif opcion == "1":
                nombre = str(input("Ingrese el nombre del nuevo Rol: "))
                resultado=rolControlador.insertarRol(nombre)
                print(resultado)

            elif opcion == "2":
                resultado=rolControlador.mostrarTodosLosRoles()
                print(resultado)

            elif opcion == "3":
                try:
                    Id = int(input("Ingrese el ID del Rol: "))
                    resultado=rolControlador.mostrarRolPorId(Id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "4":
                try:
                    id = int(input("Ingrese el ID del rol a actualizar: "))
                    nombre = str(input("Ingrese el nuevo nombre del rol: "))
                    resultado = rolControlador.actualizarRol(id, nombre)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "5":
                try:
                    id = int(input("Ingrese el ID del rol a Borrar: "))
                    resultado = rolControlador.borrarRol(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        


    def crear_tabla():
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            
            query = """
                CREATE TABLE roles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL
            );
            """
            
            cursor.execute(query)
            conexion.commit()
            print("Tabla 'roles' creada exitosamente.")
    
        except Exception as e:
            if "1050" in str(e):
                print("La tabla 'roles' ya existe.")
            else:
                print("Ocurrió un error al crear la tabla:", e)
            
        finally:
                cursor.close()
                conexion.close()




if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()