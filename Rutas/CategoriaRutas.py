from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.CategoriaControlador import CategoriaControlador

categoriaControlador=CategoriaControlador()

appCategorias = Blueprint('categorias', __name__)


@appCategorias.route('/categorias', methods=['POST'])
@ValidarToken(1,2)
def crear_categoria():
    payload = request.get_json()
    nombre = payload.get('nombre')
    respuesta: Respuesta = categoriaControlador.insertarCategoria(nombre)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@appCategorias.route('/categorias', methods=['GET'])
@ValidarToken(1,2)
def obtener_categorias():
    respuesta: Respuesta = categoriaControlador.mostrarTodasLasCategorias()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appCategorias.route('/categorias/<int:categoria_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_categoria_por_id(categoria_id):
    respuesta: Respuesta = categoriaControlador.mostrarCategoriaPorId(categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appCategorias.route('/categorias/<int:categoria_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_categoria(categoria_id):
    payload = request.get_json()
    nombre = payload.get('nombre')
    respuesta: Respuesta = categoriaControlador.actualizarCategoria(categoria_id, nombre)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appCategorias.route('/categorias/<int:categoria_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_categoria(categoria_id):
    respuesta: Respuesta = categoriaControlador.borrarCategoria(categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400
