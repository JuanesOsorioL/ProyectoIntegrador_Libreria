from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.EditorialControlador import EditorialControlador

editorialControlador=EditorialControlador()

appEditorial = Blueprint('editoriales', __name__)

@appEditorial.route('/editoriales', methods=['POST'])
@ValidarToken(1,2)
def crear_editorial():
    payload = request.get_json()
    respuesta: Respuesta = editorialControlador.insertarEditorial(payload.get('nombre'), payload.get('pais'))
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@appEditorial.route('/editoriales', methods=['GET'])
@ValidarToken(1,2)
def obtener_editoriales():
    respuesta: Respuesta = editorialControlador.mostrarTodasLasEditoriales()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appEditorial.route('/editoriales/<int:editorial_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_editorial_por_id(editorial_id):
    respuesta: Respuesta = editorialControlador.mostrarEditorialPorId(editorial_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@appEditorial.route('/editoriales/<int:editorial_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_editorial(editorial_id):
    payload = request.get_json()
    nombre = payload.get('nombre')
    pais = payload.get('pais')
    respuesta: Respuesta = editorialControlador.actualizarEditorial(editorial_id, nombre, pais)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appEditorial.route('/editoriales/<int:editorial_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_editorial(editorial_id):
    respuesta: Respuesta = editorialControlador.borrarEditorial(editorial_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400