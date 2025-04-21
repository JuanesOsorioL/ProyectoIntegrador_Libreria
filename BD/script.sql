-- Creación de usuario con permisos adecuados (más seguro)
CREATE USER 'user_biblioteca'@'localhost' IDENTIFIED BY 'B1bl10t3c4_2024!';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON db_biblioteca.* TO 'user_biblioteca'@'localhost';



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

-- =============================
-- = SECCIÓN: TABLA DEVOLUCION =
-- =============================

CREATE TABLE IF NOT EXISTS devoluciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_real_devolucion DATE NOT NULL,
    estado_libro VARCHAR(50) NOT NULL,
    observaciones TEXT
);

--Insertar
DELIMITER 
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
END;

DELIMITER ;

--Mostrar
DELIMITER 
CREATE PROCEDURE proc_select_devolucion()
BEGIN
    SELECT * FROM devoluciones;
END;

DELIMITER ;

--Mostrar por ID
DELIMITER
CREATE PROCEDURE proc_select_devolucion_por_id (
    IN p_id INT
)
BEGIN
    SELECT * FROM devoluciones WHERE id = p_id;
END;

DELIMITER ;

--Actualizar
DELIMITER 
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
END;

DELIMITER ;

--Eliminar
DELIMITER
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

-- Tabla: devoluciones
CREATE TABLE IF NOT EXISTS devoluciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_real_devolucion DATE NOT NULL,
    estado_libro VARCHAR(50) NOT NULL,
    observaciones TEXT
);




