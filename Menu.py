from Controlador.RolControlador import RolControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador
import pyodbc;
import os
import msgpack
from datetime import datetime
from Utilidades.Configuracion import Configuracion
from Dtos.UsuarioDTO import UsuarioDTO
from Dtos.Generico.Respuesta import Respuesta

rolControlador = RolControlador();
usuarioControlador = UsuarioControlador()
usuarioSistemaControlador = UsuarioSistemaControlador()

class Menu:

    token_actual = None


    def seleccionarUnRolValido(resultado)-> int:
        ids_validos = [rol.id for rol in resultado]          
        while True:

            for roldto in resultado:
                print(roldto.mostrar())

            entrada = input("ID del rol asociado: ")

            try:
                rol_id = int(entrada)
            except ValueError:
                print("Debes ingresar un número entero.")
                continue

            if rol_id not in ids_validos:
                print(f"El ID {rol_id} no está en la lista. Elige uno de los mostrados.")
                continue
            
            return entrada

    def menu():
        print("\nMenú de Opciones:")
        print("0. Creacion de tablas")
        print("1. Ingresar Rol")
        print("2. Mostrar Los Roles")
        print("3. Mostrar Rol por ID")
        print("4. Actualizar Rol por ID")
        print("5. Borrar Rol por ID")
        print("6. Ingresar Usuario")
        print("7. Mostrar Todos los Usuarios")
        print("8. Mostrar Usuario por ID")
        print("9. Mostrar Usuario por Email")
        print("10. Mostrar Usuario por Rol ID")
        print("11. Actualizar Usuario")
        print("12. Borrar Usuario")
        print("13. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion
     

    def menu_Inicial():
        print("\nBienvenido a tu libreria de confianza")
        print("\nQue deseas hacer?")
        print("0. Creacion de tablas")
        print("1. Registrar")
        print("2. Login")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion


    def mostrar_menu(self):
        os.system('cls')

        while True:
            
            opcion = Menu.menu_Inicial()
            match opcion:

                case "0":
                    os.system('cls')
                    #Menu.crear_tablas_y_procedimientos()

                case "1":
                    os.system('cls')
                    try:
                        print("\nRegistro:")
                        nombre = str(input("Nombre: "))
                        email = str(input("Email: "))
                        telefono = input("Teléfono: ")
                        direccion = input("Dirección: ")
                        fecha_input = input("Fecha de registro (YYYY-MM-DD): ")

                        try:
                            fecha_obj = datetime.strptime(fecha_input, "%Y-%m-%d").date()
                            fecha_formateada = fecha_obj.strftime("%Y-%m-%d")
                        except ValueError:
                            print("Fecha inválida. Debe estar en formato YYYY-MM-DD.")
                            continue

                        resultado=rolControlador.mostrarTodosLosRolesSeleccionar()
                        rol_id=Menu.seleccionarUnRolValido(resultado)

                        resultado = usuarioControlador.insertarUsuario(nombre, email, telefono, direccion, fecha_formateada, rol_id)

                        usuarioDto = resultado.get_resultado()  
                        usuario_id = usuarioDto.Get_Id()
                        nombre_usuario = input("Nombre de Usuario: ")
                        contrasena = input("Contraseña: ")

                        resultado_registrado=usuarioSistemaControlador.insertar(usuario_id,nombre_usuario,contrasena)

                        print(resultado)
                        print(resultado_registrado)
                    except Exception as ex:
                        print(f"Error al ingresar usuario: {ex}")

                case "2":
                    os.system('cls')
                    print("\nLoguin:")
                    #nombre_usuario = input("Nombre de Usuario: ")
                    #contrasena = input("Contraseña: ")

                    nombre_usuario="gggg1"
                    contrasena="12345ggg"
                    resultado_loguin=usuarioSistemaControlador.obtenerPorNombreUsuarioYContrasena(nombre_usuario,contrasena)
                    
                    data = msgpack.unpackb(resultado_loguin.get_resultado())
                    jwt = data["token"]
                    resultado = data["resultado"]

                    resultado_loguin.set_resultado(resultado)
                    Menu.token_actual=jwt
                    print(resultado_loguin)
                case "3":
                    os.system('cls')
                    print("Saliendo del programa...")
                    break
                case _:
                    os.system('cls')
                    print("Opción no válida, intente de nuevo.")






if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()