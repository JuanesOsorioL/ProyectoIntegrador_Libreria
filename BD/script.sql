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
CREATE PROCEDURE `libreria`.`proc_insert_rol`(
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
CREATE PROCEDURE `Libreria`.`proc_select_rol`(
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
CREATE PROCEDURE `libreria`.`proc_update_rol`(
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




