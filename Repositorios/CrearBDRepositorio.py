import pyodbc;
from Utilidades.Configuracion import Configuracion

class CrearBDRepositorio:

    def __init__(self):
        self._conn_str = Configuracion.strConnection

    def _get_cursor(self):
        conn = pyodbc.connect(self._conn_str)
        return conn, conn.cursor()

    def drop_tables(self):
        conn, cursor = self._get_cursor()
        try:
            cursor.execute("USE libreria;")
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            drops = [
                "devoluciones","detalle_prestamo","prestamos","detalle_venta",
                "ventas","usuarios_sistema","usuarios","libro_categoria",
                "libro_autor","libros","categorias","autores","roles","editoriales"
            ]
            for tbl in drops:
                cursor.execute(f"DROP TABLE IF EXISTS {tbl};")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            conn.commit()
            return True, "Tablespaces previos descartados."
        except Exception as e:
            conn.rollback()
            return False, f"Error al descartar tablas: {e}"
        finally:
            cursor.close()
            conn.close()



    def create_tables(self):
        conn, cursor = self._get_cursor()
        try:
            cursor.execute("USE libreria;")

            tablas_sql = [
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
                    nombre BLOB NOT NULL,
                    nombre_hmac CHAR(64) NOT NULL UNIQUE
                )
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
                    nombre BLOB NOT NULL,
                    nombre_hmac CHAR(64) NOT NULL,
                    email BLOB NOT NULL,
                    email_hmac CHAR(64) NOT NULL UNIQUE,
                    telefono BLOB NOT NULL,
                    telefono_hmac CHAR(64) NOT NULL,
                    direccion BLOB NOT NULL,
                    direccion_hmac CHAR(64) NOT NULL,
                    fecha_registro DATE DEFAULT CURRENT_DATE,
                    rol_id INT,
                    FOREIGN KEY (rol_id) REFERENCES roles(id))
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
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE)
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
            
            for sql in tablas_sql:
                cursor.execute(sql)
            conn.commit()
            return True, "Tablas creadas correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Error al crear tablas: {e}"
        finally:
            cursor.close()
            conn.close()



    def create_procedures(self):
        conn, cursor = self._get_cursor()
        try:
            cursor.execute("USE libreria;")

            procedimientos = [
                ("proc_insert_rol", """
                CREATE PROCEDURE `proc_insert_rol`(
                    IN p_Nombre BLOB,
                    IN p_NombreHmac CHAR(64),
                    OUT p_NuevoId INT,
                    OUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM Libreria.roles WHERE nombre_hmac = p_NombreHmac) THEN
                        SET p_Respuesta = 2;
                        SET p_NuevoId = NULL;
                    ELSE
                        INSERT INTO Libreria.roles (nombre, nombre_hmac) VALUES (p_Nombre, p_NombreHmac);
                        SET p_NuevoId = LAST_INSERT_ID();
                        SET p_Respuesta = 1;
                    END IF;
                END
                """),
                ("proc_select_rol", """
                CREATE PROCEDURE `proc_select_rol`(
                    INOUT p_Respuesta INT
                )
                BEGIN
                    SELECT id, nombre, nombre_hmac FROM Libreria.roles;
                    SET p_Respuesta = 1;
                END
                """),
                ("proc_select_rol_por_id", """
                CREATE PROCEDURE `proc_select_rol_por_id` (
                    IN p_id INT
                )
                BEGIN
                    SELECT id, nombre, nombre_hmac
                    FROM Libreria.roles
                    WHERE id = p_id;
                END
                """),
                ("proc_update_rol", """
                CREATE PROCEDURE `proc_update_rol`(
                    IN p_Id INT,
                    IN p_Nombre BLOB,
                    IN p_NombreHmac CHAR(64),
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM Libreria.roles WHERE id = p_Id) THEN
                        UPDATE Libreria.roles
                        SET nombre = p_Nombre,
                            nombre_hmac = p_NombreHmac
                        WHERE id = p_Id;

                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END
                """),
                ("proc_delete_rol", """
                CREATE PROCEDURE `proc_delete_rol`(
                    IN p_id INT,
                    INOUT p_Respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM Libreria.roles WHERE id = p_id) THEN
                        DELETE FROM Libreria.roles WHERE id = p_id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END
                """),
                ("proc_insert_usuario", """
                CREATE PROCEDURE `proc_insert_usuario`(
                    IN p_nombre BLOB,
                    IN p_nombre_hmac CHAR(64),
                    IN p_email BLOB,
                    IN p_email_hmac CHAR(64),
                    IN p_telefono BLOB,
                    IN p_telefono_hmac CHAR(64),
                    IN p_direccion BLOB,
                    IN p_direccion_hmac CHAR(64),
                    IN p_rol_id INT,
                    OUT p_nuevo_id INT,
                    OUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios WHERE email_hmac = p_email_hmac) THEN
                        SET p_respuesta = 2;
                        SET p_nuevo_id = NULL;
                    ELSE
                        INSERT INTO usuarios (
                            nombre, nombre_hmac,
                            email, email_hmac,
                            telefono, telefono_hmac,
                            direccion, direccion_hmac,
                            rol_id
                        )
                        VALUES (
                            p_nombre, p_nombre_hmac,
                            p_email, p_email_hmac,
                            p_telefono, p_telefono_hmac,
                            p_direccion, p_direccion_hmac,
                            p_rol_id
                        );

                        SET p_nuevo_id = LAST_INSERT_ID();
                        SET p_respuesta = 1;
                    END IF;
                END
                """),
                ("proc_select_usuarios", """
                CREATE PROCEDURE `proc_select_usuarios`(
                    INOUT p_respuesta INT
                )
                BEGIN
                    SELECT 
                        id,
                        nombre,
                        nombre_hmac,
                        email,
                        email_hmac,
                        telefono,
                        telefono_hmac,
                        direccion,
                        direccion_hmac,
                        fecha_registro,
                        rol_id
                    FROM usuarios;

                    SET p_respuesta = 1;
                END
                """),
                ("proc_select_usuario_por_id", """
                CREATE PROCEDURE `proc_select_usuario_por_id`(
                    IN p_id INT
                )
                BEGIN
                    SELECT 
                        id,
                        nombre,
                        nombre_hmac,
                        email,
                        email_hmac,
                        telefono,
                        telefono_hmac,
                        direccion,
                        direccion_hmac,
                        fecha_registro,
                        rol_id
                    FROM usuarios
                    WHERE id = p_id;
                END
                """),
                ("proc_update_usuario", """
               CREATE PROCEDURE `proc_update_usuario`(
                    IN p_id INT,
                    IN p_nombre BLOB,
                    IN p_nombre_hmac CHAR(64),
                    IN p_email BLOB,
                    IN p_email_hmac CHAR(64),
                    IN p_telefono BLOB,
                    IN p_telefono_hmac CHAR(64),
                    IN p_direccion BLOB,
                    IN p_direccion_hmac CHAR(64),
                    IN p_fecha_registro DATE,
                    IN p_rol_id INT,
                    INOUT p_respuesta INT
                )
                BEGIN
                    IF EXISTS (SELECT 1 FROM usuarios WHERE id = p_id) THEN
                        UPDATE usuarios
                        SET 
                            nombre = p_nombre,
                            nombre_hmac = p_nombre_hmac,
                            email = p_email,
                            email_hmac = p_email_hmac,
                            telefono = p_telefono,
                            telefono_hmac = p_telefono_hmac,
                            direccion = p_direccion,
                            direccion_hmac = p_direccion_hmac,
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
                    CREATE PROCEDURE `proc_delete_usuario`(
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
               CREATE PROCEDURE `proc_select_usuario_por_email`(
                    IN p_email_hmac CHAR(64)
                )
                BEGIN
                    SELECT 
                        id,
                        nombre,
                        nombre_hmac,
                        email,
                        email_hmac,
                        telefono,
                        telefono_hmac,
                        direccion,
                        direccion_hmac,
                        fecha_registro,
                        rol_id
                    FROM usuarios
                    WHERE email_hmac = p_email_hmac;
                END
                """),
                ("proc_select_usuarios_por_rol", """
                CREATE PROCEDURE `proc_select_usuarios_por_rol`(
                    IN p_rol_id INT
                )
                BEGIN
                    SELECT 
                        id,
                        nombre,
                        nombre_hmac,
                        email,
                        email_hmac,
                        telefono,
                        telefono_hmac,
                        direccion,
                        direccion_hmac,
                        fecha_registro,
                        rol_id
                    FROM usuarios
                    WHERE rol_id = p_rol_id;
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
                """),
                ("proc_select_usuarios_sistema_por_hmac", """
                CREATE PROCEDURE proc_select_usuarios_sistema_por_hmac(
                    IN p_hmac CHAR(64)
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
                    FROM usuarios_sistema us
                    INNER JOIN usuarios u ON us.usuario_id = u.id
                    WHERE nombre_usuario_hmac = p_hmac;
                END
                """),



                #Autores
                ("proc_insert_autor", """
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
                """),
                ("proc_select_autor", """
                CREATE PROCEDURE proc_select_autor()
                BEGIN
                    SELECT id, nombre, nacionalidad FROM autores;
                END
                """),
                ("proc_select_autor_por_id", """
                CREATE PROCEDURE proc_select_autor_por_id(IN p_id INT)
                BEGIN
                    SELECT id, nombre, nacionalidad FROM autores WHERE id = p_id;
                END
                """),
                ("proc_update_autor", """
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
                """),
                ("proc_delete_autor", """
                CREATE PROCEDURE proc_delete_autor(IN p_id INT, INOUT p_Respuesta INT)
                BEGIN
                    IF EXISTS (SELECT 1 FROM autores WHERE id = p_id) THEN
                        DELETE FROM autores WHERE id = p_id;
                        SET p_Respuesta = 1;
                    ELSE
                        SET p_Respuesta = 2;
                    END IF;
                END
                """),
                                # CATEGORIAS
                ("proc_insert_categoria", """
                    CREATE PROCEDURE `proc_insert_categoria`(
                        IN p_Nombre VARCHAR(100),
                        OUT p_NuevoId INT,
                        OUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (SELECT 1 FROM Libreria.categorias WHERE nombre = p_Nombre) THEN
                            SET p_Respuesta = 2;
                            SET p_NuevoId = NULL;
                        ELSE
                            INSERT INTO Libreria.categorias (nombre) VALUES (p_Nombre);
                            SET p_NuevoId = LAST_INSERT_ID();
                            SET p_Respuesta = 1;
                        END IF;
                    END
                """),
                ("proc_select_categoria", """
                    CREATE PROCEDURE `proc_select_categoria`()
                    BEGIN
                        SELECT id, nombre FROM Libreria.categorias;
                    END
                """),
                ("proc_select_categoria_por_id", """
                    CREATE PROCEDURE `proc_select_categoria_por_id`(
                        IN p_id INT
                    )
                    BEGIN
                        SELECT id, nombre FROM Libreria.categorias WHERE id = p_id;
                    END
                """),
                ("proc_update_categoria", """
                    CREATE PROCEDURE `proc_update_categoria`(
                        IN p_Id INT,
                        IN p_Nombre VARCHAR(100),
                        INOUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (SELECT 1 FROM Libreria.categorias WHERE id = p_Id) THEN
                            UPDATE Libreria.categorias SET nombre = p_Nombre WHERE id = p_Id;
                            SET p_Respuesta = 1;
                        ELSE
                            SET p_Respuesta = 2;
                        END IF;
                    END
                """),
                ("proc_delete_categoria", """
                    CREATE PROCEDURE `proc_delete_categoria`(
                        IN p_Id INT,
                        INOUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (SELECT 1 FROM Libreria.categorias WHERE id = p_Id) THEN
                            DELETE FROM Libreria.categorias WHERE id = p_Id;
                            SET p_Respuesta = 1;
                        ELSE
                            SET p_Respuesta = 2;
                        END IF;
                    END
                """),
                                # LIBRO-CATEGORIAS
                ("proc_insert_libro_categoria", """
                    CREATE PROCEDURE `proc_insert_libro_categoria`(
                        IN p_LibroId INT,
                        IN p_CategoriaId INT,
                        OUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (
                            SELECT 1 FROM Libreria.libros_categorias 
                            WHERE libro_id = p_LibroId AND categoria_id = p_CategoriaId
                        ) THEN
                            SET p_Respuesta = 3; -- Ya existe la relación
                        ELSE
                            INSERT INTO Libreria.libros_categorias (libro_id, categoria_id) 
                            VALUES (p_LibroId, p_CategoriaId);
                            SET p_Respuesta = 1; -- Éxito
                        END IF;
                    END
                """),
                ("proc_select_libro_categoria", """
                    CREATE PROCEDURE `proc_select_libro_categoria`()
                    BEGIN
                        SELECT libro_id, categoria_id FROM Libreria.libros_categorias;
                    END
                """),
                ("proc_select_libro_categoria_por_id", """
                    CREATE PROCEDURE `proc_select_libro_categoria_por_id`(
                        IN p_LibroId INT,
                        IN p_CategoriaId INT
                    )
                    BEGIN
                        SELECT libro_id, categoria_id 
                        FROM Libreria.libros_categorias 
                        WHERE libro_id = p_LibroId AND categoria_id = p_CategoriaId;
                    END
                """),
                ("proc_update_libro_categoria", """
                    CREATE PROCEDURE `proc_update_libro_categoria`(
                        IN p_LibroId INT,
                        IN p_CategoriaId INT,
                        IN p_NuevoLibroId INT,
                        IN p_NuevaCategoriaId INT,
                        OUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (
                            SELECT 1 FROM Libreria.libros_categorias 
                            WHERE libro_id = p_LibroId AND categoria_id = p_CategoriaId
                        ) THEN
                            UPDATE Libreria.libros_categorias 
                            SET libro_id = p_NuevoLibroId, categoria_id = p_NuevaCategoriaId
                            WHERE libro_id = p_LibroId AND categoria_id = p_CategoriaId;
                            SET p_Respuesta = 1;
                        ELSE
                            SET p_Respuesta = 2; -- No existe la relación original
                        END IF;
                    END
                """),
                ("proc_delete_libro_categoria", """
                    CREATE PROCEDURE `proc_delete_libro_categoria`(
                        IN p_LibroId INT,
                        IN p_CategoriaId INT,
                        OUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (
                            SELECT 1 FROM Libreria.libros_categorias 
                            WHERE libro_id = p_LibroId AND categoria_id = p_CategoriaId
                        ) THEN
                            DELETE FROM Libreria.libros_categorias 
                            WHERE libro_id = p_LibroId AND categoria_id = p_CategoriaId;
                            SET p_Respuesta = 1;
                        ELSE
                            SET p_Respuesta = 2; -- No existe la relación
                        END IF;
                    END
                """),
                # LIBRO AUTORES
                ("proc_insert_libro_autor", """
                    CREATE PROCEDURE `proc_insert_libro_autor`(
                        IN p_IdLibro INT,
                        IN p_IdAutor INT,
                        OUT p_NuevoId INT,
                        OUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (
                            SELECT 1 FROM Libreria.libro_autor 
                            WHERE id_libro = p_IdLibro AND id_autor = p_IdAutor
                        ) THEN
                            SET p_Respuesta = 2; -- Relación ya existe
                            SET p_NuevoId = NULL;
                        ELSE
                            INSERT INTO Libreria.libro_autor (id_libro, id_autor) 
                            VALUES (p_IdLibro, p_IdAutor);
                            SET p_NuevoId = LAST_INSERT_ID();
                            SET p_Respuesta = 1; -- Inserción exitosa
                        END IF;
                    END
                """),
                ("proc_select_libro_autor", """
                    CREATE PROCEDURE `proc_select_libro_autor`()
                    BEGIN
                        SELECT id, id_libro, id_autor FROM Libreria.libro_autor;
                    END
                """),
                ("proc_select_libro_autor_por_id", """
                    CREATE PROCEDURE `proc_select_libro_autor_por_id`(
                        IN p_Id INT
                    )
                    BEGIN
                        SELECT id, id_libro, id_autor 
                        FROM Libreria.libro_autor 
                        WHERE id = p_Id;
                    END
                """),
                ("proc_update_libro_autor", """
                    CREATE PROCEDURE `proc_update_libro_autor`(
                        IN p_Id INT,
                        IN p_IdLibro INT,
                        IN p_IdAutor INT,
                        INOUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (
                            SELECT 1 FROM Libreria.libro_autor 
                            WHERE id = p_Id
                        ) THEN
                            UPDATE Libreria.libro_autor 
                            SET id_libro = p_IdLibro, id_autor = p_IdAutor 
                            WHERE id = p_Id;
                            SET p_Respuesta = 1; -- Actualización exitosa
                        ELSE
                            SET p_Respuesta = 2; -- Relación no encontrada
                        END IF;
                    END
                """),
                ("proc_delete_libro_autor", """
                    CREATE PROCEDURE `proc_delete_libro_autor`(
                        IN p_Id INT,
                        INOUT p_Respuesta INT
                    )
                    BEGIN
                        IF EXISTS (
                            SELECT 1 FROM Libreria.libro_autor 
                            WHERE id = p_Id
                        ) THEN
                            DELETE FROM Libreria.libro_autor 
                            WHERE id = p_Id;
                            SET p_Respuesta = 1; -- Eliminación exitosa
                        ELSE
                            SET p_Respuesta = 2; -- Relación no encontrada
                        END IF;
                    END
                """),
                                    # EDITORIALES
                    ("proc_insert_editorial", """
                        CREATE PROCEDURE `proc_insert_editorial`(
                            IN p_Nombre VARCHAR(100),
                            IN p_Pais VARCHAR(50),
                            OUT p_NuevoId INT,
                            OUT p_Respuesta INT
                        )
                        BEGIN
                            IF EXISTS (
                                SELECT 1 FROM Libreria.editoriales 
                                WHERE nombre = p_Nombre
                            ) THEN
                                SET p_Respuesta = 2;
                                SET p_NuevoId = NULL;
                            ELSE
                                INSERT INTO Libreria.editoriales (nombre, pais) 
                                VALUES (p_Nombre, p_Pais);
                                SET p_NuevoId = LAST_INSERT_ID();
                                SET p_Respuesta = 1;
                            END IF;
                        END
                    """),
                    ("proc_select_editorial", """
                        CREATE PROCEDURE `proc_select_editorial`()
                        BEGIN
                            SELECT id, nombre, pais FROM Libreria.editoriales;
                        END
                    """),
                    ("proc_select_editorial_por_id", """
                        CREATE PROCEDURE `proc_select_editorial_por_id`(
                            IN p_id INT
                        )
                        BEGIN
                            SELECT id, nombre, pais 
                            FROM Libreria.editoriales 
                            WHERE id = p_id;
                        END
                    """),
                    ("proc_update_editorial", """
                        CREATE PROCEDURE `proc_update_editorial`(
                            IN p_Id INT,
                            IN p_Nombre VARCHAR(100),
                            IN p_Pais VARCHAR(50),
                            INOUT p_Respuesta INT
                        )
                        BEGIN
                            IF EXISTS (
                                SELECT 1 FROM Libreria.editoriales 
                                WHERE id = p_Id
                            ) THEN
                                UPDATE Libreria.editoriales 
                                SET nombre = p_Nombre, pais = p_Pais 
                                WHERE id = p_Id;
                                SET p_Respuesta = 1;
                            ELSE
                                SET p_Respuesta = 2;
                            END IF;
                        END
                    """),
                    ("proc_delete_editorial", """
                        CREATE PROCEDURE `proc_delete_editorial`(
                            IN p_id INT,
                            INOUT p_Respuesta INT
                        )
                        BEGIN
                            IF EXISTS (
                                SELECT 1 FROM Libreria.editoriales 
                                WHERE id = p_id
                            ) THEN
                                DELETE FROM Libreria.editoriales 
                                WHERE id = p_id;
                                SET p_Respuesta = 1;
                            ELSE
                                SET p_Respuesta = 2;
                            END IF;
                        END
                    """)


            ]





            for name, ddl in procedimientos:
                cursor.execute(f"DROP PROCEDURE IF EXISTS {name};")
                cursor.execute(ddl)
            conn.commit()
            return True, "Procedimientos almacenados creados correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Error al crear procedimientos: {e}"
        finally:
            cursor.close()
            conn.close()