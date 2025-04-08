-- Creación de usuario con permisos adecuados (más seguro)
CREATE USER 'user_biblioteca'@'localhost' IDENTIFIED BY 'B1bl10t3c4_2024!';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON db_biblioteca.* TO 'user_biblioteca'@'localhost';

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