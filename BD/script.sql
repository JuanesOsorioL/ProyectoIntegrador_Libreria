-- Creación de usuario con permisos adecuados (más seguro)
DROP USER IF EXISTS 'user_ptyhon'@'localhost';
CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT ALL PRIVILEGES ON libreria.* TO 'user_ptyhon'@'localhost';
FLUSH PRIVILEGES;


SELECT user, host FROM mysql.user WHERE user = 'user_ptyhon';
GRANT ALL PRIVILEGES ON libreria.* TO 'user_ptyhon'@'localhost';
FLUSH PRIVILEGES;

--tabla roles
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre BLOB NOT NULL,
    nombre_hmac CHAR(64) NOT NULL UNIQUE
);







--insertar rol
DELIMITER $$

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
END$$

DELIMITER ;

--mostrar todos los roles
DELIMITER $$
CREATE PROCEDURE `proc_select_rol`(
CREATE PROCEDURE `proc_select_rol`(
    INOUT p_Respuesta INT
)
BEGIN
    SELECT id, nombre, nombre_hmac FROM Libreria.roles;
    SET p_Respuesta = 1;
END$$
DELIMITER ;

--buscar rol por id
DELIMITER $$

CREATE PROCEDURE `proc_select_rol_por_id` (
    IN p_id INT
)
BEGIN
    SELECT id, nombre, nombre_hmac
    FROM Libreria.roles
    WHERE id = p_id;
END$$

DELIMITER ;

--actualizar rol
DELIMITER $$
CREATE PROCEDURE `proc_update_rol`(

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



























--tabla usuarios
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
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);



--insertar 
DELIMITER $$
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
END$$
DELIMITER ;



--mostrar todos los usuarios
DELIMITER $$
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
END$$
DELIMITER ;





--mostrar por id
DELIMITER $$
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
END$$
DELIMITER ;





--actualizar por id
DELIMITER $$
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
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- ============================================
-- 3) Consultar por hmac
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_select_usuarios_sistema_por_hmac $$
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
END $$
DELIMITER ;

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
        nombre_usuario,
        nombre_usuario_hmac,
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
        nombre_usuario,
        nombre_usuario_hmac,
        contrasena,
        salt
    FROM usuarios_sistema
    WHERE id = p_id;
END $$
DELIMITER ;



-- ============================================
-- 5) Actualizar un registro existente
-- ============================================
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_update_usuarios_sistema $$
CREATE PROCEDURE proc_update_usuarios_sistema(
    IN     p_id                  INT,
    IN     p_usuario_id          INT,
    IN     p_nombre_usuario      BLOB,
    IN     p_nombre_usuario_hmac CHAR(64),
    IN     p_contrasena          VARCHAR(32),
    IN     p_salt                VARCHAR(32),
    INOUT  p_respuesta           INT
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM usuarios_sistema WHERE id = p_id
    ) THEN
        UPDATE usuarios_sistema
        SET usuario_id         = p_usuario_id,
            nombre_usuario     = p_nombre_usuario,
            nombre_usuario_hmac = p_nombre_usuario_hmac,
            contrasena         = p_contrasena,
            salt               = p_salt
        WHERE id = p_id;
        SET p_respuesta = 1; -- actualizado
    ELSE
        SET p_respuesta = 2; -- no existe
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
        SELECT 1 FROM usuarios_sistema WHERE id = p_id
    ) THEN
        DELETE FROM usuarios_sistema WHERE id = p_id;
        SET p_respuesta = 1; -- eliminado
    ELSE
        SET p_respuesta = 2; -- no existe
    END IF;
END $$
DELIMITER ;









{
    "direccion": "calle 63 # 55-70",
    "email": "juanesosorio@hotmail.com",
    "nombre": "juan esteban osorio lopera",
    "rolId": 1,
    "telefono": "3174738789",
    "nombreUsuario": "juanes123",
    "contrasena": "abcd123"
}



{
    "direccion": "calle 63 # 55-70",
    "email": "nohemyloipera@hotmail.com",
    "nombre": "nohemy lopera herrera",
    "rolId": 2,
    "telefono": "3174738789",
    "nombreUsuario": "nohe123",
    "contrasena": "abcd123"
}



{
    "direccion": "calle 63 # 55-70",
    "email": "salome@hotmail.com",
    "nombre": "salome ramirez",
    "rolId": 3,
    "telefono": "3174738789",
    "nombreUsuario": "salo123",
    "contrasena": "abcd123"
}

{
    "direccion": "calle 44",
    "email": "carlos@hotmail.com",
    "nombre": "carlos lopez",
    "fechaRegistro": "2222-02-02",
    "rolId": 1,
    "telefono": "123456789"
}






















































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

-- Tabla: devoluciones
CREATE TABLE IF NOT EXISTS devoluciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_real_devolucion DATE NOT NULL,
    estado_libro VARCHAR(50) NOT NULL,
    observaciones TEXT
);




