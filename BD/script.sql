-- Creación de usuario con permisos adecuados (más seguro)
CREATE USER 'user_biblioteca'@'localhost' IDENTIFIED BY 'B1bl10t3c4_2024!';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON db_biblioteca.* TO 'user_biblioteca'@'localhost';

--tabla usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    fecha_registro DATE DEFAULT CURRENT_DATE,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

--insertar 
DELIMITER $$
CREATE PROCEDURE `proc_insert_usuario`(
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
END$$
DELIMITER ;

--mostrar todos los usuarios
DELIMITER $$
CREATE PROCEDURE `proc_select_usuarios`(
    INOUT p_respuesta INT
)
BEGIN
    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
    FROM usuarios;

    SET p_respuesta = 1;
END$$
DELIMITER ;

--mostrar por id
DELIMITER $$
CREATE PROCEDURE `proc_select_usuario_por_id`(
    IN p_id INT
)
BEGIN
    SELECT id, nombre, email, telefono, direccion, fecha_registro, rol_id
    FROM usuarios
    WHERE id = p_id;
END$$
DELIMITER ;

--actualizar por id
DELIMITER $$
CREATE PROCEDURE `proc_update_usuario`(
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
END$$
DELIMITER ;


--eliminar por id

DELIMITER $$
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
END$$
DELIMITER ;

--buscar por email
DELIMITER $$
CREATE PROCEDURE `proc_select_usuario_por_email`(
    IN p_email VARCHAR(100)
)
BEGIN
    SELECT 
        id,
        nombre,
        email,
        telefono,
        direccion,
        fecha_registro,
        rol_id
    FROM 
        usuarios
    WHERE 
        email = p_email;
END$$
DELIMITER ;


--buscar usuarios por id del rol
DELIMITER $$
CREATE PROCEDURE `proc_select_usuarios_por_rol`(
    IN p_rol_id INT
)
BEGIN
    SELECT 
        id,
        nombre,
        email,
        telefono,
        direccion,
        fecha_registro,
        rol_id
    FROM 
        usuarios
    WHERE 
        rol_id = p_rol_id;
END$$
DELIMITER ;



-- Tabla usuarios_sistema (login)
CREATE TABLE IF NOT EXISTS usuarios_sistema (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- insertar
DELIMITER $$
CREATE PROCEDURE proc_insert_usuarios_sistema(
    IN p_usuario_id INT,
    IN p_username VARCHAR(50),
    IN p_password_hash VARCHAR(255),
    OUT p_nuevo_id INT,
    OUT p_respuesta INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE username = p_username) THEN
        SET p_respuesta = 2;
        SET p_nuevo_id = NULL;
    ELSE
        INSERT INTO usuarios_sistema (usuario_id, username, password_hash)
        VALUES (p_usuario_id, p_username, p_password_hash);
        SET p_nuevo_id = LAST_INSERT_ID();
        SET p_respuesta = 1;
    END IF;
END$$
DELIMITER ;

-- mostrar todos
DELIMITER $$
CREATE PROCEDURE proc_select_usuarios_sistema()
BEGIN
    SELECT id, usuario_id, username, password_hash FROM usuarios_sistema;
END$$
DELIMITER ;

-- por ID
DELIMITER $$
CREATE PROCEDURE proc_select_usuarios_sistema_por_id(IN p_id INT)
BEGIN
    SELECT id, usuario_id, username, password_hash
    FROM usuarios_sistema
    WHERE id = p_id;
END$$
DELIMITER ;

-- por username
DELIMITER $$
CREATE PROCEDURE proc_select_usuarios_sistema_por_username(IN p_username VARCHAR(50))
BEGIN
    SELECT id, usuario_id, username, password_hash
    FROM usuarios_sistema
    WHERE username = p_username;
END$$
DELIMITER ;

-- actualizar
DELIMITER $$
CREATE PROCEDURE proc_update_usuarios_sistema(
    IN p_id INT,
    IN p_usuario_id INT,
    IN p_username VARCHAR(50),
    IN p_password_hash VARCHAR(255),
    INOUT p_respuesta INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE id = p_id) THEN
        UPDATE usuarios_sistema
        SET usuario_id = p_usuario_id,
            username = p_username,
            password_hash = p_password_hash
        WHERE id = p_id;
        SET p_respuesta = 1;
    ELSE
        SET p_respuesta = 2;
    END IF;
END$$
DELIMITER ;

-- eliminar
DELIMITER $$
CREATE PROCEDURE proc_delete_usuarios_sistema(IN p_id INT, INOUT p_respuesta INT)
BEGIN
    IF EXISTS (SELECT 1 FROM usuarios_sistema WHERE id = p_id) THEN
        DELETE FROM usuarios_sistema WHERE id = p_id;
        SET p_respuesta = 1;
    ELSE
        SET p_respuesta = 2;
    END IF;
END$$
DELIMITER ;











--tabla roles
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

--insertar rol
DELIMITER $$
CREATE PROCEDURE `proc_insert_rol`(
    IN p_Nombre VARCHAR(50),
    OUT p_NuevoId INT,
    OUT p_Respuesta INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM Libreria.roles WHERE Nombre = p_Nombre) THEN
        SET p_Respuesta = 2;
        SET p_NuevoId = NULL;
    ELSE
        INSERT INTO Libreria.roles (Nombre) VALUES (p_Nombre);
        SET p_NuevoId = LAST_INSERT_ID();
        SET p_Respuesta = 1;
    END IF;
END$$
DELIMITER ;

--mostrar todos los roles
DELIMITER $$
CREATE PROCEDURE `proc_select_rol`(
    INOUT p_Respuesta INT
)
BEGIN
    SELECT id, Nombre FROM Libreria.roles;
    SET p_Respuesta = 1;
END$$
DELIMITER ;

--buscar rol por id
DELIMITER $$
CREATE PROCEDURE `proc_select_rol_por_id` (
    IN p_id INT
)
BEGIN
    SELECT 
        id,
        Nombre
    FROM 
        Libreria.roles
    WHERE 
        id = p_id;
END$$
DELIMITER ;

--actualizar rol
DELIMITER $$
CREATE PROCEDURE `proc_update_rol`(
    IN p_Id INT,
    IN p_Nombre VARCHAR(50),
    INOUT p_Respuesta INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM Libreria.roles WHERE id = p_Id) THEN
        UPDATE Libreria.roles
        SET Nombre = p_Nombre
        WHERE id = p_Id;

        SET p_Respuesta = 1;
    ELSE
        SET p_Respuesta = 2;
    END IF;
END$$
DELIMITER ;

--borrar rol
DELIMITER $$
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
END$$
DELIMITER ;














-- Creación de la base de datos
CREATE DATABASE db_biblioteca;
USE db_biblioteca;

-- 1. Configuración inicial
CREATE DATABASE db_biblioteca_14;
USE db_biblioteca_14;

-- 1. Tabla de Roles
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    puede_prestar BOOLEAN DEFAULT FALSE,
    puede_reservar BOOLEAN DEFAULT TRUE,
    max_libros INT DEFAULT 3
);

-- 2. Tabla de Usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_rol INT NOT NULL,
    codigo_usuario VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro DATE NOT NULL,
    fecha_expiracion DATE,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_rol) REFERENCES roles(id)
); 




