from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.AutorControlador import AutorControlador

autorControlador=AutorControlador()

appAutores = Blueprint('autores', __name__)


@appAutores.route('/autores', methods=['POST'])
@ValidarToken(1,2)
def crear_autor():
    payload = request.get_json()
    nombre = payload.get('nombre')
    nacionalidad = payload.get('nacionalidad')
    respuesta: Respuesta = autorControlador.insertarAutor(nombre, nacionalidad)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@appAutores.route('/autores', methods=['GET'])
@ValidarToken(1,2)
def obtener_autores():
    respuesta: Respuesta = autorControlador.mostrarTodosLosAutores()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appAutores.route('/autores/<int:autor_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_autor_por_id(autor_id):
    respuesta: Respuesta = autorControlador.mostrarAutorPorId(autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appAutores.route('/autores/<int:autor_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_autor(autor_id):
    payload = request.get_json()
    nombre = payload.get('nombre')
    nacionalidad = payload.get('nacionalidad')
    respuesta: Respuesta = autorControlador.actualizarAutor(autor_id, nombre, nacionalidad)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appAutores.route('/autores/<int:autor_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_autor(autor_id):
    respuesta: Respuesta = autorControlador.borrarAutor(autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400