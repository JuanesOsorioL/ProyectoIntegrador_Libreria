-- Creación de usuario con permisos adecuados (más seguro)
CREATE USER 'user_biblioteca'@'localhost' IDENTIFIED BY 'B1bl10t3c4_2024!';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON db_biblioteca.* TO 'user_biblioteca'@'localhost';

-- Creación de la base de datos
CREATE DATABASE db_biblioteca;
USE db_biblioteca;

-- Tabla de autores
CREATE TABLE autores (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    nacionalidad VARCHAR(50),
    biografia TEXT,
    PRIMARY KEY (id)
);

-- Tabla de editoriales
CREATE TABLE editoriales (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    pais VARCHAR(50),
    fundacion YEAR,
    PRIMARY KEY (id)
);