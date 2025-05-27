from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.LibroCategoriaControlador import LibroCategoriaControlador

libroCategoriaControlador=LibroCategoriaControlador()

appLibroCategoria = Blueprint('libros-categorias', __name__)

@appLibroCategoria.route('/libros-categorias', methods=['POST'])
@ValidarToken(1)
def crear_libro_categoria():
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    categoria_id = payload.get('categoria_id')
    respuesta: Respuesta = libroCategoriaControlador.insertarLibroCategoria(libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400


@appLibroCategoria.route('/libros-categorias', methods=['GET'])
@ValidarToken(1)
def obtener_libros_categorias():
    respuesta: Respuesta = libroCategoriaControlador.mostrarTodosLosLibroCategoria()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@appLibroCategoria.route('/libros-categorias/<int:libro_id>/<int:categoria_id>', methods=['GET'])
@ValidarToken(1)
def obtener_libro_categoria_por_id(libro_id, categoria_id):
    respuesta: Respuesta = libroCategoriaControlador.mostrarLibroCategoriaPorId(libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@appLibroCategoria.route('/libros-categorias/<int:libro_id>/<int:categoria_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_libro_categoria(libro_id, categoria_id):
    respuesta: Respuesta = libroCategoriaControlador.borrarLibroCategoria(libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400



@appLibroCategoria.route('/libros-categorias/<int:id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_libro_categoria(id):
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    categoria_id = payload.get('categoria_id')
    respuesta: Respuesta = libroCategoriaControlador.actualizarLibroCategoria(id, libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

