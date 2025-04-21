from Controlador.RolControlador import RolControlador
import pyodbc;
from Utilidades.Configuracion import Configuracion
from Controlador.EditorialControlador import EditorialControlador
editorialControlador = EditorialControlador();
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
            print("15. Ingresar Editorial")
            print("16. Mostrar todas las Editoriales")
            print("17. Mostrar Editorial por ID")
            print("18. Actualizar Editorial por ID")
            print("19. Borrar Editorial por ID")
            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                Menu.crear_tablas_y_procedimientos()

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
            
            elif opcion == "15":
                nombre = input("Ingrese el nombre de la Editorial: ")
                pais = input("Ingrese el país de la Editorial: ")
                resultado = editorialControlador.insertarEditorial(nombre, pais)
                print(resultado)

            elif opcion == "16":
                resultado = editorialControlador.mostrarTodasLasEditoriales()
                print(resultado)

            elif opcion == "17":
                try:
                    id = int(input("Ingrese el ID de la Editorial: "))
                    resultado = editorialControlador.mostrarEditorialPorId(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "18":
                try:
                    id = int(input("Ingrese el ID de la editorial a actualizar: "))
                    nombre = input("Ingrese el nuevo nombre de la editorial: ")
                    pais = input("Ingrese el nuevo país de la editorial: ")
                    resultado = editorialControlador.actualizarEditorial(id, nombre, pais)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "19":
                try:
                    id = int(input("Ingrese el ID de la editorial a borrar: "))
                    resultado = editorialControlador.borrarEditorial(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")                                      

            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        



    def crear_tablas_y_procedimientos():
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            # --- Crear tablas ---
            tablas = [
                """
                CREATE TABLE IF NOT EXISTS roles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS editoriales (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    pais VARCHAR(50)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS autores (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL,
                    nacionalidad VARCHAR(50)
                )
                """,
                """
                CREATE TABLE categorias (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(50) NOT NULL
                )
                """,
                """
                CREATE TABLE libros (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    titulo VARCHAR(150) NOT NULL,
                    isbn VARCHAR(20) UNIQUE,
                    descripcion TEXT,
                    anio_publicacion YEAR,
                    formato ENUM('Físico', 'Digital'),
                    editorial_id INT,
                    precio DECIMAL(10,2),
                    stock INT,
                    FOREIGN KEY (editorial_id) REFERENCES editoriales(id)
                )
                """,
                """
                CREATE TABLE libro_autor (
                    libro_id INT,
                    autor_id INT,
                    PRIMARY KEY (libro_id, autor_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (autor_id) REFERENCES autores(id)
                )
                """,
                """
                CREATE TABLE libro_categoria (
                    libro_id INT,
                    categoria_id INT,
                    PRIMARY KEY (libro_id, categoria_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                )
                """
            ]

            for sql in tablas:
                cursor.execute(sql)

            print("Tablas creadas correctamente.")

        

            # --- Crear procedimientos almacenados ---
            procedimientos = [
                # Insertar rol
                """
                DROP PROCEDURE IF EXISTS proc_insert_rol
                """,
                """
                CREATE PROCEDURE proc_insert_rol(
                    IN p_Nombre VARCHAR(50),
                    OUT p_NuevoId INT,
                    OUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM roles WHERE nombre = p_Nombre) THEN
                        SET p_Respuesta = 2;
                        SET p_NuevoId = NULL;
                    ELSE
                        INSERT INTO roles (nombre) VALUES (p_Nombre);
                        SET p_NuevoId = LAST_INSERT_ID();
                        SET p_Respuesta = 1;
                    END IF;
                END
                """,

                # Mostrar roles
                """
                DROP PROCEDURE IF EXISTS proc_select_rol
                """,
                """
                CREATE PROCEDURE proc_select_rol(
                    INOUT p_Respuesta INT
                )
                BEGIN
                    SELECT id, nombre FROM roles;
                    SET p_Respuesta = 1;
                END
                """,

                # Buscar por ID
                """
                DROP PROCEDURE IF EXISTS proc_select_rol_por_id
                """,
                """
                CREATE PROCEDURE proc_select_rol_por_id (
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre FROM roles WHERE id = p_id;
                END
                """,

                # Actualizar rol
                """
                DROP PROCEDURE IF EXISTS proc_update_rol
                """,
                """
                CREATE PROCEDURE proc_update_rol(
                    IN p_Id INT,
                    IN p_Nombre VARCHAR(50),
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM roles WHERE id = p_Id) THEN
                        UPDATE roles
                        SET nombre = p_Nombre
                        WHERE id = p_Id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END
                """,

                # Borrar rol
                """
                DROP PROCEDURE IF EXISTS proc_delete_rol
                """,
                """
                CREATE PROCEDURE proc_delete_rol(
                    IN p_id INT,
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM roles WHERE id = p_id) THEN
                        DELETE FROM roles WHERE id = p_id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END
                """
                ,
                #Insertar editorial
                """
                DROP PROCEDURE IF EXISTS proc_insert_editorial;
                """
                ,

                """
                CREATE PROCEDURE proc_insert_editorial(
                    IN p_Nombre VARCHAR(100),
                    IN p_Pais VARCHAR(50),
                    OUT p_NuevoId INT,
                    OUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM editoriales WHERE nombre = p_Nombre) THEN
                        SET p_Respuesta = 2;
                        SET p_NuevoId = NULL;
                    ELSE
                        INSERT INTO editoriales (nombre, pais) VALUES (p_Nombre, p_Pais);
                        SET p_NuevoId = LAST_INSERT_ID();
                        SET p_Respuesta = 1;
                    END IF;
                END;
                """,

                #Seleccionar todas las editoriales
                """        
                DROP PROCEDURE IF EXISTS proc_select_editorial;
                """,
                """
                CREATE PROCEDURE proc_select_editorial()
                BEGIN
                    SELECT id, nombre, pais FROM editoriales;
                END;
                """,

                #Seleccionar editorial por ID
                """
                DROP PROCEDURE IF EXISTS proc_select_editorial_por_id;
                """,
                """
                CREATE PROCEDURE proc_select_editorial_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre, pais FROM editoriales WHERE id = p_id;
                END;
                """,

                #Actualizar editorial
                """
                DROP PROCEDURE IF EXISTS proc_update_editorial;
                """,
                """
                CREATE PROCEDURE proc_update_editorial(
                    IN p_Id INT,
                    IN p_Nombre VARCHAR(100),
                    IN p_Pais VARCHAR(50),
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM editoriales WHERE id = p_Id) THEN
                        UPDATE editoriales
                        SET nombre = p_Nombre,
                            pais = p_Pais
                        WHERE id = p_Id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END;
                """,

                #Borrar editorial
                """
                DROP PROCEDURE IF EXISTS proc_delete_editorial;
                """,
                """
                CREATE PROCEDURE proc_delete_editorial(
                    IN p_id INT,
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM editoriales WHERE id = p_id) THEN
                        DELETE FROM editoriales WHERE id = p_id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END;
                """

            ]

            for proc in procedimientos:
                cursor.execute(proc)

            conexion.commit()
            print("Procedimientos almacenados creados correctamente.")

        except Exception as e:
            print("❌ Error:", e)

        finally:
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()