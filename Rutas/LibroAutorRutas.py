from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.LibroAutorControlador import LibroAutorControlador
libroAutorControlador=LibroAutorControlador()

appLibroAutores = Blueprint('libros-autores', __name__)


@appLibroAutores.route('/libros-autores', methods=['POST'])
@ValidarToken(1)
def crear_libro_autor():
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    autor_id = payload.get('autor_id')
    respuesta: Respuesta = libroAutorControlador.insertarLibroAutor(libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@appLibroAutores.route('/libros-autores', methods=['GET'])
@ValidarToken(1)
def obtener_libros_autores():
    respuesta: Respuesta = libroAutorControlador.mostrarTodosLosLibroAutor()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@appLibroAutores.route('/libros-autores/<int:libro_id>/<int:autor_id>', methods=['GET'])
@ValidarToken(1)
def obtener_libro_autor_por_id(libro_id, autor_id):
    respuesta: Respuesta = libroAutorControlador.mostrarLibroAutorPorId(libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@appLibroAutores.route('/libros-autores/<int:libro_id>/<int:autor_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_libro_autor(libro_id, autor_id):
    respuesta: Respuesta = libroAutorControlador.borrarLibroAutor(libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400


@appLibroAutores.route('/libros-autores/<int:libro_id>/<int:autor_id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_libro_autor(antes_libro_id, antes_autor_id):
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    autor_id = payload.get('autor_id')
    respuesta: Respuesta = libroAutorControlador.actualizarLibroAutor(libro_id, autor_id,antes_libro_id, antes_autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400
