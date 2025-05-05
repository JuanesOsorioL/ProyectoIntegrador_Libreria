-- Creación de usuario con permisos adecuados (más seguro)
DROP USER IF EXISTS 'user_ptyhon'@'localhost';
CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT ALL PRIVILEGES ON libreria.* TO 'user_ptyhon'@'localhost';
FLUSH PRIVILEGES;





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













-- Tabla usuarios_sistema (login) SIN rol_id
CREATE TABLE IF NOT EXISTS usuarios_sistema (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    nombre_usuario BLOB NOT NULL,
    nombre_usuario_hmac CHAR(64) NOT NULL UNIQUE,
    contrasena VARCHAR(32) NOT NULL,
    salt VARCHAR(32) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- ============================================
-- 1) Insertar nuevo registro con payload MsgPack + HMAC
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_insert_usuarios_sistema $$
CREATE PROCEDURE proc_insert_usuarios_sistema(
    IN  p_usuario_id         INT,
    IN  p_username_payload   BLOB,
    IN  p_username_hmac      CHAR(64),
    IN  p_contrasena         VARCHAR(32),
    IN  p_salt               VARCHAR(32),
    OUT p_nuevo_id           INT,
    OUT p_respuesta          INT
)
BEGIN
    IF EXISTS (
        SELECT 1
          FROM usuarios_sistema
         WHERE username_hmac = p_username_hmac
    ) THEN
        SET p_respuesta = 2;
        SET p_nuevo_id  = NULL;
    ELSE
        INSERT INTO usuarios_sistema
            (usuario_id, username_payload, username_hmac, contrasena, salt)
        VALUES
            (p_usuario_id, p_username_payload, p_username_hmac, p_contrasena, p_salt);
        SET p_nuevo_id  = LAST_INSERT_ID();
        SET p_respuesta = 1;
    END IF;
END $$
DELIMITER ;

-- ============================================
-- 2) Listar todos los registros
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_select_usuarios_sistema $$
CREATE PROCEDURE proc_select_usuarios_sistema()
BEGIN
    SELECT
        id,
        usuario_id,
        username_payload,
        username_hmac,
        contrasena,
        salt
      FROM usuarios_sistema;
END $$
DELIMITER ;

-- ============================================
-- 3) Consultar por ID
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_select_usuarios_sistema_por_id $$
CREATE PROCEDURE proc_select_usuarios_sistema_por_id(
    IN p_id INT
)
BEGIN
    SELECT
        id,
        usuario_id,
        username_payload,
        username_hmac,
        contrasena,
        salt
      FROM usuarios_sistema
     WHERE id = p_id;
END $$
DELIMITER ;

-- ============================================
-- 4) Consultar por HMAC (indicador único)
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_select_usuarios_sistema_por_hmac $$
CREATE PROCEDURE proc_select_usuarios_sistema_por_hmac(
    IN p_username_hmac CHAR(64)
)
BEGIN
    SELECT
        id,
        usuario_id,
        username_payload,
        username_hmac,
        contrasena,
        salt
      FROM usuarios_sistema
     WHERE username_hmac = p_username_hmac;
END $$
DELIMITER ;

-- ============================================
-- 5) Actualizar un registro existente
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_update_usuarios_sistema $$
CREATE PROCEDURE proc_update_usuarios_sistema(
    IN     p_id                 INT,
    IN     p_usuario_id         INT,
    IN     p_username_payload   BLOB,
    IN     p_username_hmac      CHAR(64),
    IN     p_contrasena         VARCHAR(32),
    IN     p_salt               VARCHAR(32),
    INOUT  p_respuesta          INT
)
BEGIN
    IF EXISTS (
        SELECT 1
          FROM usuarios_sistema
         WHERE id = p_id
    ) THEN
        UPDATE usuarios_sistema
           SET usuario_id        = p_usuario_id,
               username_payload  = p_username_payload,
               username_hmac     = p_username_hmac,
               contrasena        = p_contrasena,
               salt              = p_salt
         WHERE id = p_id;
        SET p_respuesta = 1;    -- actualizado
    ELSE
        SET p_respuesta = 2;    -- no existe el id
    END IF;
END $$
DELIMITER ;

-- ============================================
-- 6) Eliminar un registro
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_delete_usuarios_sistema $$
CREATE PROCEDURE proc_delete_usuarios_sistema(
    IN    p_id        INT,
    INOUT p_respuesta INT
)
BEGIN
    IF EXISTS (
        SELECT 1
          FROM usuarios_sistema
         WHERE id = p_id
    ) THEN
        DELETE FROM usuarios_sistema
         WHERE id = p_id;
        SET p_respuesta = 1;    -- eliminado
    ELSE
        SET p_respuesta = 2;    -- no existe
    END IF;
END $$
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




