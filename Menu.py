from Controlador.RolControlador import RolControlador
import pyodbc;
from Utilidades.Configuracion import Configuracion

rolControlador:RolControlador=RolControlador();

from Controlador.DevolucionControlador import DevolucionControlador

devolucionControlador = DevolucionControlador()

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
            print("10. Ingresar Devolución")
            print("11. Mostrar Todas las Devoluciones")
            print("12. Mostrar Devolución por ID")
            print("13. Actualizar Devolución por ID")
            print("14. Borrar Devolución por ID")
            print("7. Salir")
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
            elif opcion == "10":
                fecha = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
                estado = input("Estado del libro (Bueno / Dañado / Perdido): ")
                observaciones = input("Observaciones: ")
                resultado = devolucionControlador.insertarDevolucion(fecha, estado, observaciones)
                print(resultado)

            elif opcion == "11":
                resultado = devolucionControlador.mostrarTodasLasDevoluciones()
                print(resultado)

            elif opcion == "12":
                try:
                    id = int(input("Ingrese el ID de la devolución: "))
                    resultado = devolucionControlador.mostrarDevolucionPorId(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "13":
                try:
                    id = int(input("ID de la devolución a actualizar: "))
                    fecha = input("Nueva fecha de devolución (YYYY-MM-DD): ")
                    estado = input("Nuevo estado del libro (Bueno / Dañado / Perdido): ")
                    observaciones = input("Nuevas observaciones: ")
                    resultado = devolucionControlador.actualizarDevolucion(id, fecha, estado, observaciones)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "14":
                try:
                    id = int(input("ID de la devolución a borrar: "))
                    resultado = devolucionControlador.borrarDevolucion(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "7":
                    print("Saliendo del programa...")
                    break
            else:
                    print("Opción no válida, intente de nuevo.")
        

    @staticmethod
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
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS devoluciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha_real_devolucion DATE NOT NULL,
                estado_libro VARCHAR(50) NOT NULL,
                observaciones TEXT
            );
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
                """,
                # ----------------------------
                # PROCEDIMIENTOS: DEVOLUCION    
                # ----------------------------
                """
                DROP PROCEDURE IF EXISTS proc_insert_devolucion;
                """,
                """
                CREATE PROCEDURE proc_insert_devolucion (
                    IN p_fecha DATE,
                    IN p_estado VARCHAR(50),
                    IN p_observaciones TEXT,
                    OUT p_NuevoId INT,
                    OUT p_Respuesta INT
                )
                BEGIN
                    DECLARE EXIT HANDLER FOR SQLEXCEPTION SET p_Respuesta = 0;
                    INSERT INTO devoluciones (fecha_real_devolucion, estado_libro, observaciones)
                    VALUES (p_fecha, p_estado, p_observaciones);
                    SET p_NuevoId = LAST_INSERT_ID();
                    SET p_Respuesta = 1;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_select_devolucion;
                """,
                """
                CREATE PROCEDURE proc_select_devolucion()
                BEGIN
                    SELECT * FROM devoluciones;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_select_devolucion_por_id;
                """,
                """
                CREATE PROCEDURE proc_select_devolucion_por_id (
                    IN p_id INT
                )
                BEGIN
                    SELECT * FROM devoluciones WHERE id = p_id;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_update_devolucion;
                """,
                """
                CREATE PROCEDURE proc_update_devolucion (
                    IN p_id INT,
                    IN p_fecha DATE,
                    IN p_estado VARCHAR(50),
                    IN p_observaciones TEXT,
                    OUT Respuesta INT
                )
                BEGIN
                    DECLARE EXIT HANDLER FOR SQLEXCEPTION SET Respuesta = 0;

                    UPDATE devoluciones
                    SET fecha_real_devolucion = p_fecha,
                        estado_libro = p_estado,
                        observaciones = p_observaciones
                    WHERE id = p_id;

                    IF ROW_COUNT() > 0 THEN
                        SET Respuesta = 1;
                    ELSE
                        SET Respuesta = 2;
                    END IF;
                END
                """,
                """
                DROP PROCEDURE IF EXISTS proc_delete_devolucion;
                """,
                """
                CREATE PROCEDURE proc_delete_devolucion (
                    IN p_id INT,
                    OUT Respuesta INT
                )
                BEGIN
                    DELETE FROM devoluciones WHERE id = p_id;

                    IF ROW_COUNT() > 0 THEN
                        SET Respuesta = 1;
                    ELSE
                        SET Respuesta = 2;
                    END IF;
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