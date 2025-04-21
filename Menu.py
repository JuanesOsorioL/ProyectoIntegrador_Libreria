from Controlador.RolControlador import RolControlador
import pyodbc;
import os
from Utilidades.Configuracion import Configuracion

rolControlador = RolControlador();

class Menu:

    def menu():
        print("\nMenú de Opciones:")
        print("0. Creacion de tablas")
        print("1. Ingresar Rol")
        print("2. Mostrar Los Roles")
        print("3. Mostrar Rol por ID")
        print("4. Actualizar Rol por ID")
        print("5. Borrar Rol por ID")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion


    def mostrar_menu(self):
        os.system('cls')

        while True:
            
            opcion = Menu.menu()
            
            if opcion == "0":
                os.system('cls')
                Menu.crear_tablas_y_procedimientos()

            elif opcion == "1":
                os.system('cls')
                nombre = str(input("Ingrese el nombre del nuevo Rol: "))
                resultado=rolControlador.insertarRol(nombre)
                print(resultado)

            elif opcion == "2":
                os.system('cls')               
                resultado=rolControlador.mostrarTodosLosRoles()
                print(resultado)

            elif opcion == "3":
                os.system('cls')
                try:
                    Id = int(input("Ingrese el ID del Rol: "))
                    resultado=rolControlador.mostrarRolPorId(Id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "4":
                os.system('cls')
                try:
                    id = int(input("Ingrese el ID del rol a actualizar: "))
                    nombre = str(input("Ingrese el nuevo nombre del rol: "))
                    resultado = rolControlador.actualizarRol(id, nombre)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "5":
                os.system('cls')
                try:
                    id = int(input("Ingrese el ID del rol a Borrar: "))
                    resultado = rolControlador.borrarRol(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")
            
            elif opcion == "6":
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
                CREATE TABLE IF NOT EXISTS editoriales (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    pais VARCHAR(50)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS autores (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    nacionalidad VARCHAR(50)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS categorias (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS libros (
                    id INT AUTO_INCREMENT PRIMARY KEY,
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
                CREATE TABLE IF NOT EXISTS libro_autor (
                    libro_id INT,
                    autor_id INT,
                    PRIMARY KEY (libro_id, autor_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (autor_id) REFERENCES autores(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS libro_categoria (
                    libro_id INT,
                    categoria_id INT,
                    PRIMARY KEY (libro_id, categoria_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS roles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    telefono VARCHAR(20),
                    direccion VARCHAR(200),
                    fecha_registro DATE DEFAULT CURRENT_DATE,
                    rol_id INT,
                    FOREIGN KEY (rol_id) REFERENCES roles(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS usuarios_sistema (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS ventas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    empleado_id INT NOT NULL,
                    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
                    total DECIMAL(10,2),
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY (empleado_id) REFERENCES usuarios(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS detalle_venta (
                    venta_id INT,
                    libro_id INT,
                    cantidad INT,
                    precio_unitario DECIMAL(10,2),
                    subtotal DECIMAL(10,2),
                    PRIMARY KEY (venta_id, libro_id),
                    FOREIGN KEY (venta_id) REFERENCES ventas(id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS prestamos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    empleado_id INT NOT NULL,
                    fecha_prestamo DATE,
                    fecha_devolucion DATE,
                    estado VARCHAR(20),
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY (empleado_id) REFERENCES usuarios(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS detalle_prestamo (
                    prestamo_id INT,
                    libro_id INT,
                    cantidad INT,
                    PRIMARY KEY (prestamo_id, libro_id),
                    FOREIGN KEY (prestamo_id) REFERENCES prestamos(id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id)
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS devoluciones (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    prestamo_id INT NOT NULL,
                    fecha_real_devolucion DATE,
                    estado_libro VARCHAR(20),
                    observaciones TEXT,
                    FOREIGN KEY (prestamo_id) REFERENCES prestamos(id)
                )
                """
            ]

            for sql in tablas:
                cursor.execute(sql)

            print("Tablas creadas correctamente.")

            # --- Crear procedimientos almacenados ---
            procedimientos = [
                # ----------------------------
                # PROCEDIMIENTOS: ROLES
                # ----------------------------
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
                """,
                # ----------------------------
                # PROCEDIMIENTOS: USUARIOS
                # ----------------------------
                """
                DROP PROCEDURE IF EXISTS proc_insert_usuario
                """,
                """
                CREATE PROCEDURE proc_insert_usuario(
                    IN p_nombre VARCHAR(100),
                    IN p_email VARCHAR(100),
                    IN p_telefono VARCHAR(20),
                    IN p_direccion VARCHAR(255),
                    IN p_fecha_registro DATE,
                    IN p_rol_id INT,
                    OUT p_nuevo_id INT,
                    OUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios WHERE email = p_email) THEN
                        SET p_respuesta = 2;
                        SET p_nuevo_id = NULL;
                    ELSE
                        INSERT INTO usuarios (nombre, email, telefono, direccion, fecha_registro, rol_id)
                        VALUES (p_nombre, p_email, p_telefono, p_direccion, p_fecha_registro, p_rol_id);

                        SET p_nuevo_id = LAST_INSERT_ID();
                        SET p_respuesta = 1;
                    END IF;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_select_usuarios
                """,
                """
                CREATE PROCEDURE proc_select_usuarios(
                    INOUT p_respuesta INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios;
                    SET p_respuesta = 1;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_select_usuario_por_id
                """,
                """
                CREATE PROCEDURE proc_select_usuario_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios
                    WHERE id = p_id;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_update_usuario
                """,
                """
                CREATE PROCEDURE proc_update_usuario(
                    IN p_id INT,
                    IN p_nombre VARCHAR(100),
                    IN p_email VARCHAR(100),
                    IN p_telefono VARCHAR(20),
                    IN p_direccion VARCHAR(255),
                    IN p_fecha_registro DATE,
                    IN p_rol_id INT,
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios WHERE id = p_id) THEN
                        UPDATE usuarios
                        SET nombre = p_nombre,
                            email = p_email,
                            telefono = p_telefono,
                            direccion = p_direccion,
                            fecha_registro = p_fecha_registro,
                            rol_id = p_rol_id
                        WHERE id = p_id;

                        SET p_respuesta = 1;
                    ELSE
                        SET p_respuesta = 2;
                    END IF;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_delete_usuario
                """,
                """
                CREATE PROCEDURE proc_delete_usuario(
                    IN p_id INT,
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios WHERE id = p_id) THEN
                        DELETE FROM usuarios WHERE id = p_id;
                        SET p_respuesta = 1;
                    ELSE
                        SET p_respuesta = 2;
                    END IF;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_select_usuario_por_email
                """,
                """
                CREATE PROCEDURE proc_select_usuario_por_email(
                    IN p_email VARCHAR(100)
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios
                    WHERE email = p_email;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_select_usuarios_por_rol
                """,
                """
                CREATE PROCEDURE proc_select_usuarios_por_rol(
                    IN p_rol_id INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios
                    WHERE rol_id = p_rol_id;
                END
                """
            ]

            for proc in procedimientos:
                cursor.execute(proc)

            conexion.commit()
            print("Procedimientos almacenados creados correctamente.")

        except Exception as e:
            if "1050" in str(e):
                print("La tablas ya existe.")
            else:
                print("Ocurrió un error al crear la tabla:", e)

        finally:
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()