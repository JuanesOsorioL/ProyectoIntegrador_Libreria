from Controlador.RolControlador import RolControlador
import pyodbc;
import os
from Utilidades.Configuracion import Configuracion
from Controlador.DevolucionControlador import DevolucionControlador
from Controlador.EditorialControlador import EditorialControlador
from Controlador.AutorControlador import AutorControlador
from Controlador.CategoriaControlador import CategoriaControlador
from Controlador.LibroAutorControlador import LibroAutorControlador

categoriaControlador = CategoriaControlador()
editorialControlador = EditorialControlador();
rolControlador = RolControlador();
devolucionControlador = DevolucionControlador()
autorControlador = AutorControlador()
libroAutorControlador =LibroAutorControlador()  


class Menu:

    def menu():
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
        print("15. Ingresar Editorial")
        print("16. Mostrar todas las Editoriales")
        print("17. Mostrar Editorial por ID")
        print("18. Actualizar Editorial por ID")
        print("19. Borrar Editorial por ID")
        print("20. Ingresar Autor")
        print("21. Mostrar Todos los Autores")
        print("22. Mostrar Autor por ID")
        print("23. Actualizar Autor por ID")
        print("24. Borrar Autor por ID")
        print("25. Ingresar Categoría")
        print("26. Mostrar Todas las Categorías")
        print("27. Mostrar Categoría por ID")
        print("28. Actualizar Categoría por ID")
        print("29. Borrar Categoría por ID")
        print("30. Ingresar Libro-Autor")
        print("31. Mostrar Todos los Libro-Autor")
        print("32. Mostrar Libro-Autor por ID")
        print("33. Actualizar Libro-Autor por ID")
        print("34. Borrar Libro-Autor por ID")
        print("35. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion


    def mostrar_menu(self):
        os.system('cls')

        while True:
            
            opcion = Menu.menu()
            
            if opcion == "0":
                os.system('cls')
                
                crear_tablas_y_procedimientos()

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

            
            elif opcion == "20":
                nombre = input("Ingrese el nombre del Autor: ")
                nacionalidad = input("Ingrese la nacionalidad del Autor: ")
                resultado = autorControlador.insertarAutor(nombre, nacionalidad)
                print(resultado)

            elif opcion == "21":
                resultado = autorControlador.mostrarTodosLosAutores()
                print(resultado)

            elif opcion == "22":
                try:
                    id = int(input("Ingrese el ID del Autor: "))
                    resultado = autorControlador.mostrarAutorPorId(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "23":
                try:
                    id = int(input("Ingrese el ID del autor a actualizar: "))
                    nombre = input("Ingrese el nuevo nombre del autor: ")
                    nacionalidad = input("Ingrese la nueva nacionalidad del autor: ")
                    resultado = autorControlador.actualizarAutor(id, nombre, nacionalidad)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "24":
                try:
                    id = int(input("Ingrese el ID del autor a borrar: "))
                    resultado = autorControlador.borrarAutor(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "25":
                nombre = input("Ingrese el nombre de la Categoría: ")
                descripcion = input("Ingrese la descripción de la Categoría: ")
                resultado = categoriaControlador.insertarCategoria(nombre, descripcion)
                print(resultado)

            elif opcion == "26":
                resultado = categoriaControlador.mostrarTodasLasCategorias()
                print(resultado)

            elif opcion == "27":
                try:
                    id = int(input("Ingrese el ID de la Categoría: "))
                    resultado = categoriaControlador.mostrarCategoriaPorId(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "28":
                try:
                    id = int(input("Ingrese el ID de la categoría a actualizar: "))
                    nombre = input("Ingrese el nuevo nombre de la categoría: ")
                    descripcion = input("Ingrese la nueva descripción: ")
                    resultado = categoriaControlador.actualizarCategoria(id, nombre, descripcion)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "29":
                try:
                    id = int(input("Ingrese el ID de la categoría a borrar: "))
                    resultado = categoriaControlador.borrarCategoria(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "30":
                try:
                    id_libro = int(input("Ingrese el ID del libro: "))
                    id_autor = int(input("Ingrese el ID del autor: "))
                    resultado = libroAutorControlador.insertarLibroAutor(id_libro, id_autor)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "31":
                resultado = libroAutorControlador.mostrarTodosLosLibroAutor()
                print(resultado)

            elif opcion == "32":
                try:
                    id = int(input("Ingrese el ID del libro autor: "))
                    resultado = libroAutorControlador.mostrarLibroAutorPorId(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "33":
                try:
                    id = int(input("Ingrese el ID del libro autor a actualizar: "))
                    id_libro = int(input("Ingrese el nuevo ID del libro: "))
                    id_autor = int(input("Ingrese el nuevo ID del autor: "))
                    resultado = libroAutorControlador.actualizarLibroAutor(id, id_libro, id_autor)
                    print(resultado)
                except ValueError:
                    print("Datos inválidos.")

            elif opcion == "34":
                try:
                    id = int(input("Ingrese el ID del libro autor a borrar: "))
                    resultado = libroAutorControlador.borrarLibroAutor(id)
                    print(resultado)
                except ValueError:
                    print("ID inválido.")

            elif opcion == "35":
                print("Saliendo del programa...")
                break

            else:
                    print("Opción no válida, intente de nuevo.")
        

def crear_tablas_y_procedimientos():
    try:
        conexion = pyodbc.connect(Configuracion.strConnection)
        cursor = conexion.cursor()

        # --- CREAR TABLAS ---
        tablas = [
            # ROLES
            """
            CREATE TABLE IF NOT EXISTS roles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL
            )
            """,

            # USUARIOS Y USUARIOS_SISTEMA
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

            # EDITORIALES
            """
            CREATE TABLE IF NOT EXISTS editoriales (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                pais VARCHAR(50)
            )
            """,

            # AUTORES
            """
            CREATE TABLE IF NOT EXISTS autores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                nacionalidad VARCHAR(50)
            )
            """,

            # CATEGORÍAS
            """
            CREATE TABLE IF NOT EXISTS categorias (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL
            )
            """,

            # LIBROS Y RELACIONES
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

            # VENTAS
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

            # PRÉSTAMOS
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

            # DEVOLUCIONES
            """
            CREATE TABLE IF NOT EXISTS devoluciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha_real_devolucion DATE,
                estado_libro VARCHAR(50),
                observaciones TEXT
            )
            """
        ]

#prestamo_id INT,
#FOREIGN KEY (prestamo_id) REFERENCES prestamos(id)

        for sql in tablas:
            cursor.execute(sql)

        print("✅ Tablas creadas correctamente.")

        # --- PROCEDIMIENTOS ALMACENADOS ---
        procedimientos = [

            # ROLES
            "DROP PROCEDURE IF EXISTS proc_insert_rol",
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
            "DROP PROCEDURE IF EXISTS proc_select_rol",
            """
            CREATE PROCEDURE proc_select_rol(INOUT p_Respuesta INT)
            BEGIN
                SELECT id, nombre FROM roles;
                SET p_Respuesta = 1;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_rol_por_id",
            """
            CREATE PROCEDURE proc_select_rol_por_id(IN p_id INT)
            BEGIN
                SELECT id, nombre FROM roles WHERE id = p_id;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_update_rol",
            """
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
            """,
            "DROP PROCEDURE IF EXISTS proc_delete_rol",
            """
            CREATE PROCEDURE proc_delete_rol(IN p_id INT, INOUT p_Respuesta INT)
            BEGIN
                IF EXISTS (SELECT 1 FROM roles WHERE id = p_id) THEN
                    DELETE FROM roles WHERE id = p_id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,

            # USUARIOS
            "DROP PROCEDURE IF EXISTS proc_insert_usuario",
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
            "DROP PROCEDURE IF EXISTS proc_select_usuarios",
            """
            CREATE PROCEDURE proc_select_usuarios(INOUT p_respuesta INT)
            BEGIN
                SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id FROM usuarios;
                SET p_respuesta = 1;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_usuario_por_id",
            """
            CREATE PROCEDURE proc_select_usuario_por_id(IN p_id INT)
            BEGIN
                SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id FROM usuarios WHERE id = p_id;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_usuario_por_email",
            """
            CREATE PROCEDURE proc_select_usuario_por_email(IN p_email VARCHAR(100))
            BEGIN
                SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id FROM usuarios WHERE email = p_email;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_update_usuario",
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
                    UPDATE usuarios SET
                        nombre = p_nombre,
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
            "DROP PROCEDURE IF EXISTS proc_delete_usuario",
            """
            CREATE PROCEDURE proc_delete_usuario(IN p_id INT, INOUT p_respuesta INT)
            BEGIN
                IF EXISTS (SELECT 1 FROM usuarios WHERE id = p_id) THEN
                    DELETE FROM usuarios WHERE id = p_id;
                    SET p_respuesta = 1;
                ELSE
                    SET p_respuesta = 2;
                END IF;
            END
            """,

            # EDITORIALES
            "DROP PROCEDURE IF EXISTS proc_insert_editorial",
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
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_editorial",
            """
            CREATE PROCEDURE proc_select_editorial()
            BEGIN
                SELECT id, nombre, pais FROM editoriales;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_editorial_por_id",
            """
            CREATE PROCEDURE proc_select_editorial_por_id(IN p_id INT)
            BEGIN
                SELECT id, nombre, pais FROM editoriales WHERE id = p_id;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_update_editorial",
            """
            CREATE PROCEDURE proc_update_editorial(
                IN p_Id INT,
                IN p_Nombre VARCHAR(100),
                IN p_Pais VARCHAR(50),
                INOUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM editoriales WHERE id = p_Id) THEN
                    UPDATE editoriales SET nombre = p_Nombre, pais = p_Pais WHERE id = p_Id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_delete_editorial",
            """
            CREATE PROCEDURE proc_delete_editorial(IN p_id INT, INOUT p_Respuesta INT)
            BEGIN
                IF EXISTS (SELECT 1 FROM editoriales WHERE id = p_id) THEN
                    DELETE FROM editoriales WHERE id = p_id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,

            #CATEGORIAS
            "DROP PROCEDURE IF EXISTS proc_insert_categoria",
            """
            CREATE PROCEDURE proc_insert_categoria(
                IN p_Nombre VARCHAR(100),
                OUT p_NuevoId INT,
                OUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM categorias WHERE nombre = p_Nombre) THEN
                    SET p_Respuesta = 2;
                    SET p_NuevoId = NULL;
                ELSE
                    INSERT INTO categorias (nombre) VALUES (p_Nombre);
                    SET p_NuevoId = LAST_INSERT_ID();
                    SET p_Respuesta = 1;
                END IF;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_categoria",
            """
            CREATE PROCEDURE proc_select_categoria()
            BEGIN
                SELECT id, nombre FROM categorias;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_categoria_por_id",
            """
            CREATE PROCEDURE proc_select_categoria_por_id(IN p_id INT)
            BEGIN
                SELECT id, nombre FROM categorias WHERE id = p_id;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_update_categoria",
            """
            CREATE PROCEDURE proc_update_categoria(
                IN p_Id INT,
                IN p_Nombre VARCHAR(100),
                INOUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM categorias WHERE id = p_Id) THEN
                    UPDATE categorias SET nombre = p_Nombre WHERE id = p_Id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_delete_categoria",
            """
            CREATE PROCEDURE proc_delete_categoria(
                IN p_Id INT,
                INOUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM categorias WHERE id = p_Id) THEN
                    DELETE FROM categorias WHERE id = p_Id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,

            #AUTORES
            
            "DROP PROCEDURE IF EXISTS proc_insert_autor",
            """
            CREATE PROCEDURE proc_insert_autor(
                IN p_Nombre VARCHAR(100),
                IN p_Nacionalidad VARCHAR(50),
                OUT p_NuevoId INT,
                OUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM autores WHERE nombre = p_Nombre) THEN
                    SET p_Respuesta = 2;
                    SET p_NuevoId = NULL;
                ELSE
                    INSERT INTO autores (nombre, nacionalidad) VALUES (p_Nombre, p_Nacionalidad);
                    SET p_NuevoId = LAST_INSERT_ID();
                    SET p_Respuesta = 1;
                END IF;
            END
        
            """,

            
            "DROP PROCEDURE IF EXISTS proc_select_autor",
            """
            CREATE PROCEDURE proc_select_autor()
            BEGIN
                SELECT id, nombre, nacionalidad FROM autores;
            END
            """,

           
            "DROP PROCEDURE IF EXISTS proc_select_autor_por_id",
            """
            CREATE PROCEDURE proc_select_autor_por_id(IN p_id INT)
            BEGIN
                SELECT id, nombre, nacionalidad FROM autores WHERE id = p_id;
            END
            """,

            
            "DROP PROCEDURE IF EXISTS proc_update_autor",
            """
            CREATE PROCEDURE proc_update_autor(
                IN p_Id INT,
                IN p_Nombre VARCHAR(100),
                IN p_Nacionalidad VARCHAR(50),
                INOUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM autores WHERE id = p_Id) THEN
                    UPDATE autores SET nombre = p_Nombre, nacionalidad = p_Nacionalidad WHERE id = p_Id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,

            
            "DROP PROCEDURE IF EXISTS proc_delete_autor",
            """
            CREATE PROCEDURE proc_delete_autor(IN p_id INT, INOUT p_Respuesta INT)
            BEGIN
                IF EXISTS (SELECT 1 FROM autores WHERE id = p_id) THEN
                    DELETE FROM autores WHERE id = p_id;
                    SET p_Respuesta = 1;
                ELSE
                    SET p_Respuesta = 2;
                END IF;
            END
            """,
            #Libro Autores

            "DROP PROCEDURE IF EXISTS proc_insert_libro_autor",
            """
            CREATE PROCEDURE proc_insert_libro_autor(
                IN p_IdLibro INT,
                IN p_IdAutor INT,
                OUT p_NuevoId INT,
                OUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM libro_autor WHERE id_libro = p_IdLibro AND id_autor = p_IdAutor) THEN
                    SET p_Respuesta = 2; -- Relación ya existe
                    SET p_NuevoId = NULL;
                ELSE
                    INSERT INTO libro_autor (id_libro, id_autor) VALUES (p_IdLibro, p_IdAutor);
                    SET p_NuevoId = LAST_INSERT_ID();
                    SET p_Respuesta = 1; -- Inserción exitosa
                END IF;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_libro_autor",
            """
            CREATE PROCEDURE proc_select_libro_autor()
            BEGIN
                SELECT id, id_libro, id_autor FROM libro_autor;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_select_libro_autor_por_id",
            """
            CREATE PROCEDURE proc_select_libro_autor_por_id(IN p_Id INT)
            BEGIN
                SELECT id, id_libro, id_autor FROM libro_autor WHERE id = p_Id;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_update_libro_autor",
            """
            CREATE PROCEDURE proc_update_libro_autor(
                IN p_Id INT,
                IN p_IdLibro INT,
                IN p_IdAutor INT,
                INOUT p_Respuesta INT
            )
            BEGIN
                IF EXISTS (SELECT 1 FROM libro_autor WHERE id = p_Id) THEN
                    UPDATE libro_autor SET id_libro = p_IdLibro, id_autor = p_IdAutor WHERE id = p_Id;
                    SET p_Respuesta = 1; -- Actualización exitosa
                ELSE
                    SET p_Respuesta = 2; -- Relación no encontrada
                END IF;
            END
            """,
            "DROP PROCEDURE IF EXISTS proc_delete_libro_autor",
            """
            CREATE PROCEDURE proc_delete_libro_autor(IN p_Id INT, INOUT p_Respuesta INT)
            BEGIN
                IF EXISTS (SELECT 1 FROM libro_autor WHERE id = p_Id) THEN
                    DELETE FROM libro_autor WHERE id = p_Id;
                    SET p_Respuesta = 1; -- Eliminación exitosa
                ELSE
                    SET p_Respuesta = 2; -- Relación no encontrada
                END IF;
            END
            """,

            #devoluciones
            
            """
            CREATE PROCEDURE proc_insert_devolucion (
                IN p_fecha DATE,
                IN p_estado VARCHAR(50),
                IN p_observaciones TEXT,
                OUT p_NuevoId INT,
                OUT p_Respuesta INT
            )
            BEGIN
                DECLARE EXIT HANDLER FOR SQLEXCEPTION
                BEGIN
                    SET p_Respuesta = 0;
                END;

                INSERT INTO devoluciones (fecha_real_devolucion, estado_libro, observaciones)
                VALUES (p_fecha, p_estado, p_observaciones);

                SET p_NuevoId = LAST_INSERT_ID();
                SET p_Respuesta = 1;
            END
            """,
            """
            CREATE PROCEDURE proc_select_devolucion()
            BEGIN
                SELECT * FROM devoluciones;
            END
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
            CREATE PROCEDURE proc_update_devolucion (
                IN p_id INT,
                IN p_fecha DATE,
                IN p_estado VARCHAR(50),
                IN p_observaciones TEXT,
                OUT Respuesta INT
            )
            BEGIN
                DECLARE EXIT HANDLER FOR SQLEXCEPTION
                BEGIN
                    SET Respuesta = 0;
                END;

                UPDATE devoluciones
                SET fecha_real_devolucion = p_fecha,
                    estado_libro = p_estado,
                    observaciones = p_observaciones
                WHERE id = p_id;

                IF ROW_COUNT() > 0 THEN
                    SET Respuesta = 1;
                ELSE
                    SET Respuesta = 2; -- No se encontró
                END IF;
            END
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
            END;

            """
        ]

        for proc in procedimientos:
            cursor.execute(proc)

        conexion.commit()
        print("✅ Procedimientos almacenados creados correctamente.")

    except Exception as e:
        print("❌ Error al crear tablas o procedimientos:", e)

    finally:
        cursor.close()
        conexion.close()


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()