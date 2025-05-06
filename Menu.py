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
                    Menu.crear_tablas_y_procedimientos()

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








    """ 
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
                os.system('cls')
                try:
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
                    
                    rol_id = int(input("ID del rol asociado: "))
                    resultado = usuarioControlador.insertarUsuario(nombre, email, telefono, direccion, fecha_formateada, rol_id)
                    print(resultado)
                except Exception as ex:
                    print(f"Error al ingresar usuario: {ex}")

            elif opcion == "7":
                os.system('cls')
                resultado = usuarioControlador.mostrarTodosLosUsuarios()
                print(resultado)

            elif opcion == "8":
                os.system('cls')
                try:
                    id = int(input("Ingrese el ID del Usuario: "))
                    resultado = usuarioControlador.mostrarUsuarioPorId(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "9":
                os.system('cls')
                email = input("Ingrese el Email del usuario: ")
                resultado = usuarioControlador.mostrarUsuarioPorEmail(email)
                print(resultado)
            
            elif opcion == "10":
                os.system('cls')
                id_Rol = input("Ingrese el ID Rol: ")
                resultado = usuarioControlador.mostrarUsuarioPorRolId(id_Rol)
                print(resultado)

            elif opcion == "11":
                os.system('cls')
                try:
                    id = int(input("ID del usuario a actualizar: "))
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    telefono = input("Teléfono: ")
                    direccion = input("Dirección: ")
                    fecha_input = input("Fecha de registro (YYYY-MM-DD): ")
                    try:
                        fecha_obj = datetime.strptime(fecha_input, "%Y-%m-%d").date()
                        fecha_formateada = fecha_obj.strftime("%Y-%m-%d")
                    except ValueError:
                        print("Fecha inválida. Use formato YYYY-MM-DD.")
                        continue
                    rol_id = int(input("ID del rol: "))
                    resultado = usuarioControlador.actualizarUsuario(id, nombre, email, telefono, direccion, fecha_formateada, rol_id)
                    print(resultado)
                except Exception as ex:
                    print(f"Error al actualizar usuario: {ex}")

            elif opcion == "12":
                os.system('cls')
                try:
                    id = int(input("Ingrese el ID del Usuario a borrar: "))
                    resultado = usuarioControlador.borrarUsuario(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "13":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        """        

    def crear_tablas_y_procedimientos_vieho():
        try:
            # Conectarse a la base de datos
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("USE libreria;")

            # --- 1) Crear tablas ---
            tablas = [
                # Editoriales
                """
                CREATE TABLE IF NOT EXISTS editoriales (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    pais VARCHAR(50)
                )
                """,
                # Roles
                """
                CREATE TABLE IF NOT EXISTS roles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL UNIQUE
                )
                """,
                # Autores
                """
                CREATE TABLE IF NOT EXISTS autores (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    nacionalidad VARCHAR(50)
                )
                """,
                # Categorías
                """
                CREATE TABLE IF NOT EXISTS categorias (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL
                )
                """,
                # Libros
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
                # Libro–Autor (N:M)
                """
                CREATE TABLE IF NOT EXISTS libro_autor (
                    libro_id INT,
                    autor_id INT,
                    PRIMARY KEY (libro_id, autor_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (autor_id) REFERENCES autores(id)
                )
                """,
                # Libro–Categoría (N:M)
                """
                CREATE TABLE IF NOT EXISTS libro_categoria (
                    libro_id INT,
                    categoria_id INT,
                    PRIMARY KEY (libro_id, categoria_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                )
                """,
                # Usuarios
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
                # Usuarios del sistema (credenciales)
                """
                CREATE TABLE IF NOT EXISTS usuarios_sistema (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT,
                    nombre_usuario BLOB NOT NULL,
                    nombre_usuario_hmac CHAR(64) NOT NULL UNIQUE,
                    contrasena CHAR(64) NOT NULL,
                    salt CHAR(32) NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )
                """,
                # Ventas
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
                # Detalle de venta
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
                # Préstamos
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
                # Detalle de préstamo
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
                # Devoluciones
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
            conexion.commit()
            print("Tablas creadas correctamente.")

            # --- 2) Crear procedimientos almacenados ---
            procedimientos = [
                # ROLES
                ("proc_insert_rol", """
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
                """),
                ("proc_select_rol", """
                CREATE PROCEDURE proc_select_rol(
                    INOUT p_Respuesta INT
                )
                BEGIN
                    SELECT id, nombre FROM roles;
                    SET p_Respuesta = 1;
                END
                """),
                ("proc_select_rol_por_id", """
                CREATE PROCEDURE proc_select_rol_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre FROM roles WHERE id = p_id;
                END
                """),
                ("proc_update_rol", """
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
                """),
                ("proc_delete_rol", """
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
                """),

                # USUARIOS
                ("proc_insert_usuario", """
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
                """),
                ("proc_select_usuarios", """
                CREATE PROCEDURE proc_select_usuarios(
                    INOUT p_respuesta INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios;
                    SET p_respuesta = 1;
                END
                """),
                ("proc_select_usuario_por_id", """
                CREATE PROCEDURE proc_select_usuario_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios
                    WHERE id = p_id;
                END
                """),
                ("proc_update_usuario", """
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
                """),
                ("proc_delete_usuario", """
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
                """),
                ("proc_select_usuario_por_email", """
                CREATE PROCEDURE proc_select_usuario_por_email(
                    IN p_email VARCHAR(100)
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios
                    WHERE email = p_email;
                END
                """),
                ("proc_select_usuarios_por_rol", """
                CREATE PROCEDURE proc_select_usuarios_por_rol(
                    IN p_rol_id INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios
                    WHERE rol_id = p_rol_id;
                END
                """),

                # USUARIOS_SISTEMA

                ("proc_select_usuarios_sistema_por_hmac", """
                CREATE PROCEDURE proc_select_usuarios_sistema_por_hmac(
                    IN p_hmac INT
                )
                BEGIN
                    SELECT
                        us.id,
                        us.usuario_id,
                        us.nombre_usuario,
                        us.nombre_usuario_hmac,
                        us.contrasena,
                        us.salt,
                        u.rol_id
                    FROM usuarios_sistema AS us
                    INNER JOIN usuarios AS u
                        ON us.usuario_id = u.id
                    WHERE us.nombre_usuario_hmac = p_hmac;
                END
                """),


                ("proc_delete_usuarios_sistema", """
                CREATE PROCEDURE proc_delete_usuarios_sistema(
                    IN p_id INT,
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE id = p_id) THEN
                        DELETE FROM usuarios_sistema WHERE id = p_id;
                        SET p_respuesta = 1;
                    ELSE
                        SET p_respuesta = 2;
                    END IF;
                END
                """),
                ("proc_update_usuarios_sistema", """
                CREATE PROCEDURE proc_update_usuarios_sistema(
                    IN p_id INT,
                    IN p_usuario_id INT,
                    IN p_nombre_usuario BLOB,
                    IN p_nombre_usuario_hmac CHAR(64),
                    IN p_contrasena VARCHAR(32),
                    IN p_salt VARCHAR(32),
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE id = p_id) THEN
                        UPDATE usuarios_sistema
                        SET usuario_id       = p_usuario_id,
                            nombre_usuario = p_nombre_usuario,
                            nombre_usuario_hmac    = p_nombre_usuario_hmac,
                            contrasena       = p_contrasena,
                            salt             = p_salt
                        WHERE id = p_id;
                        SET p_respuesta = 1;
                    ELSE
                        SET p_respuesta = 2;
                    END IF;
                END
                """),
         
                ("proc_select_usuarios_sistema_por_id", """
                CREATE PROCEDURE proc_select_usuarios_sistema_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, usuario_id, nombre_usuario, nombre_usuario_hmac, contrasena, salt
                    FROM usuarios_sistema
                    WHERE id = p_id;
                END
                """),
                ("proc_select_usuarios_sistema", """
                CREATE PROCEDURE proc_select_usuarios_sistema()
                BEGIN
                    SELECT id, usuario_id, nombre_usuario, nombre_usuario_hmac, contrasena, salt
                    FROM usuarios_sistema;
                END
                """),
                ("proc_insert_usuarios_sistema", """
                CREATE PROCEDURE proc_insert_usuarios_sistema(
                    IN p_usuario_id INT,
                    IN p_nombre_usuario BLOB,
                    IN p_nombre_usuario_hmac CHAR(64),
                    IN p_contrasena VARCHAR(32),
                    IN p_salt VARCHAR(32),
                    OUT p_nuevo_id INT,
                    OUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE nombre_usuario_hmac = p_nombre_usuario_hmac) THEN
                        SET p_respuesta = 2;
                        SET p_nuevo_id  = NULL;
                    ELSE
                        INSERT INTO usuarios_sistema
                            (usuario_id, nombre_usuario, nombre_usuario_hmac, contrasena, salt)
                        VALUES
                            (p_usuario_id, p_nombre_usuario, p_nombre_usuario_hmac, p_contrasena, p_salt);
                        SET p_nuevo_id  = LAST_INSERT_ID();
                        SET p_respuesta = 1;
                    END IF;
                END
                """)
            ]

            for name, ddl in procedimientos:
                cursor.execute(f"DROP PROCEDURE IF EXISTS {name};")
                cursor.execute(ddl)
            conexion.commit()
            print("Procedimientos almacenados creados correctamente.")

            # --- 3) Insertar datos iniciales ---
            InsertarRoles = [
                "INSERT INTO libreria.roles (nombre) VALUES ('Administrador');",
                "INSERT INTO libreria.roles (nombre) VALUES ('Cliente');"
            ]
            for insert in InsertarRoles:
                cursor.execute(insert)
            conexion.commit()
            print("Roles creados correctamente.")

        except Exception as e:
            msg = str(e)
            if "1050" in msg:
                print("Las tablas ya existen.")
            else:
                print("Ocurrió un error al crear las tablas o procedimientos:", e)
        finally:
            cursor.close()
            conexion.close()


    def crear_tablas_y_procedimientos():
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("USE libreria;")


            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            drops = [
                "devoluciones",
                "detalle_prestamo",
                "prestamos",
                "detalle_venta",
                "ventas",
                "usuarios_sistema",
                "usuarios",
                "libro_categoria",
                "libro_autor",
                "libros",
                "categorias",
                "autores",
                "roles",
                "editoriales"
            ]
            for tbl in drops:
                cursor.execute(f"DROP TABLE IF EXISTS {tbl};")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            conexion.commit()
            print("Tablespaces previos descartados.")

            # 1) Crear tablas
            tablas = [
                # Editoriales
                """
                CREATE TABLE editoriales (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    pais VARCHAR(50)
                ) ENGINE=InnoDB;
                """,
                # Roles
                """
                CREATE TABLE roles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL UNIQUE
                ) ENGINE=InnoDB;
                """,
                # Autores
                """
                CREATE TABLE autores (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    nacionalidad VARCHAR(50)
                ) ENGINE=InnoDB;
                """,
                # Categorías
                """
                CREATE TABLE categorias (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL
                ) ENGINE=InnoDB;
                """,
                # Libros
                """
                CREATE TABLE libros (
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
                ) ENGINE=InnoDB;
                """,
                # Libro–Autor
                """
                CREATE TABLE libro_autor (
                    libro_id INT,
                    autor_id INT,
                    PRIMARY KEY (libro_id, autor_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (autor_id) REFERENCES autores(id)
                ) ENGINE=InnoDB;
                """,
                # Libro–Categoría
                """
                CREATE TABLE libro_categoria (
                    libro_id INT,
                    categoria_id INT,
                    PRIMARY KEY (libro_id, categoria_id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id),
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                ) ENGINE=InnoDB;
                """,
                # Usuarios
                """
                CREATE TABLE usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    telefono VARCHAR(20),
                    direccion VARCHAR(200),
                    fecha_registro DATE DEFAULT CURRENT_DATE,
                    rol_id INT,
                    FOREIGN KEY (rol_id) REFERENCES roles(id)
                ) ENGINE=InnoDB;
                """,
                # Usuarios del sistema
                """
                CREATE TABLE usuarios_sistema (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT,
                    nombre_usuario BLOB NOT NULL,
                    nombre_usuario_hmac CHAR(64) NOT NULL UNIQUE,
                    contrasena CHAR(64) NOT NULL,
                    salt CHAR(32) NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                ) ENGINE=InnoDB;
                """,
                # Ventas
                """
                CREATE TABLE ventas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    empleado_id INT NOT NULL,
                    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
                    total DECIMAL(10,2),
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY (empleado_id) REFERENCES usuarios(id)
                ) ENGINE=InnoDB;
                """,
                # Detalle de venta
                """
                CREATE TABLE detalle_venta (
                    venta_id INT,
                    libro_id INT,
                    cantidad INT,
                    precio_unitario DECIMAL(10,2),
                    subtotal DECIMAL(10,2),
                    PRIMARY KEY (venta_id, libro_id),
                    FOREIGN KEY (venta_id) REFERENCES ventas(id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id)
                ) ENGINE=InnoDB;
                """,
                # Préstamos
                """
                CREATE TABLE prestamos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    empleado_id INT NOT NULL,
                    fecha_prestamo DATE,
                    fecha_devolucion DATE,
                    estado VARCHAR(20),
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY (empleado_id) REFERENCES usuarios(id)
                ) ENGINE=InnoDB;
                """,
                # Detalle de préstamo
                """
                CREATE TABLE detalle_prestamo (
                    prestamo_id INT,
                    libro_id INT,
                    cantidad INT,
                    PRIMARY KEY (prestamo_id, libro_id),
                    FOREIGN KEY (prestamo_id) REFERENCES prestamos(id),
                    FOREIGN KEY (libro_id) REFERENCES libros(id)
                ) ENGINE=InnoDB;
                """,
                # Devoluciones
                """
                CREATE TABLE devoluciones (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    prestamo_id INT NOT NULL,
                    fecha_real_devolucion DATE,
                    estado_libro VARCHAR(20),
                    observaciones TEXT,
                    FOREIGN KEY (prestamo_id) REFERENCES prestamos(id)
                ) ENGINE=InnoDB;
                """
            ]

            for sql in tablas:
                cursor.execute(sql)
            conexion.commit()
            print("Tablas creadas correctamente.")


            procedimientos = [
                ("proc_insert_rol", """
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
                """),
                ("proc_select_rol", """
                CREATE PROCEDURE proc_select_rol(
                    INOUT p_Respuesta INT
                )
                BEGIN
                    SELECT id, nombre FROM roles;
                    SET p_Respuesta = 1;
                END
                """),
                ("proc_select_rol_por_id", """
                CREATE PROCEDURE proc_select_rol_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre FROM roles WHERE id = p_id;
                END
                """),
                ("proc_update_rol", """
                CREATE PROCEDURE proc_update_rol(
                    IN p_Id INT,
                    IN p_Nombre VARCHAR(50),
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM roles WHERE id = p_Id) THEN
                        UPDATE roles SET nombre = p_Nombre WHERE id = p_Id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END
                """),
                ("proc_delete_rol", """
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
                """),
                ("proc_insert_usuario", """
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
                """),
                ("proc_select_usuarios", """
                CREATE PROCEDURE proc_select_usuarios(
                    INOUT p_respuesta INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios;
                    SET p_respuesta = 1;
                END
                """),
                ("proc_select_usuario_por_id", """
                CREATE PROCEDURE proc_select_usuario_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios WHERE id = p_id;
                END
                """),
                ("proc_update_usuario", """
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
                """),
                ("proc_delete_usuario", """
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
                """),
                ("proc_select_usuario_por_email", """
                CREATE PROCEDURE proc_select_usuario_por_email(
                    IN p_email VARCHAR(100)
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios WHERE email = p_email;
                END
                """),
                ("proc_select_usuarios_por_rol", """
                CREATE PROCEDURE proc_select_usuarios_por_rol(
                    IN p_rol_id INT
                )
                BEGIN
                    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
                    FROM usuarios WHERE rol_id = p_rol_id;
                END
                """),
                ("proc_delete_usuarios_sistema", """
                CREATE PROCEDURE proc_delete_usuarios_sistema(
                    IN p_id INT,
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE id = p_id) THEN
                        DELETE FROM usuarios_sistema WHERE id = p_id;
                        SET p_respuesta = 1;
                    ELSE
                        SET p_respuesta = 2;
                    END IF;
                END
                """),
                ("proc_update_usuarios_sistema", """
                CREATE PROCEDURE proc_update_usuarios_sistema(
                    IN p_id INT,
                    IN p_usuario_id INT,
                    IN p_nombre_usuario BLOB,
                    IN p_nombre_usuario_hmac CHAR(64),
                    IN p_contrasena VARCHAR(32),
                    IN p_salt VARCHAR(32),
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE id = p_id) THEN
                        UPDATE usuarios_sistema
                        SET usuario_id       = p_usuario_id,
                            nombre_usuario = p_nombre_usuario,
                            nombre_usuario_hmac    = p_nombre_usuario_hmac,
                            contrasena       = p_contrasena,
                            salt             = p_salt
                        WHERE id = p_id;
                        SET p_respuesta = 1;
                    ELSE
                        SET p_respuesta = 2;
                    END IF;
                END
                """),

                ("proc_select_usuarios_sistema_por_id", """
                CREATE PROCEDURE proc_select_usuarios_sistema_por_id(
                    IN p_id INT
                )
                BEGIN
                    SELECT id, usuario_id, nombre_usuario, nombre_usuario_hmac, contrasena, salt
                    FROM usuarios_sistema
                    WHERE id = p_id;
                END
                """),
                ("proc_select_usuarios_sistema", """
                CREATE PROCEDURE proc_select_usuarios_sistema()
                BEGIN
                    SELECT id, usuario_id, nombre_usuario, nombre_usuario_hmac, contrasena, salt
                    FROM usuarios_sistema;
                END
                """),
                ("proc_insert_usuarios_sistema", """
                CREATE PROCEDURE proc_insert_usuarios_sistema(
                    IN p_usuario_id INT,
                    IN p_nombre_usuario BLOB,
                    IN p_nombre_usuario_hmac CHAR(64),
                    IN p_contrasena VARCHAR(32),
                    IN p_salt VARCHAR(32),
                    OUT p_nuevo_id INT,
                    OUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE nombre_usuario_hmac = p_nombre_usuario_hmac) THEN
                        SET p_respuesta = 2;
                        SET p_nuevo_id  = NULL;
                    ELSE
                        INSERT INTO usuarios_sistema
                            (usuario_id, nombre_usuario, nombre_usuario_hmac, contrasena, salt)
                        VALUES
                            (p_usuario_id, p_nombre_usuario, p_nombre_usuario_hmac, p_contrasena, p_salt);
                        SET p_nuevo_id  = LAST_INSERT_ID();
                        SET p_respuesta = 1;
                    END IF;
                END
                """)
            ]

            for name, ddl in procedimientos:
                cursor.execute(f"DROP PROCEDURE IF EXISTS {name};")
                cursor.execute(ddl)
            conexion.commit()
            print("Procedimientos almacenados creados correctamente.")

            inserts = [
                "INSERT INTO libreria.roles (nombre) VALUES ('Administrador');",
                "INSERT INTO libreria.roles (nombre) VALUES ('Cliente');"
            ]
            for ins in inserts:
                cursor.execute(ins)
            conexion.commit()
            print("Roles iniciales insertados correctamente.")

        except Exception as e:
            print("Error al crear tablas/procedimientos:", e)
        finally:
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()