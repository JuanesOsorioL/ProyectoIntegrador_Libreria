from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.RolControlador import RolControlador

rolControlador = RolControlador()

appRoles = Blueprint('roles', __name__)



@appRoles.route('/roles', methods=['GET'])
@ValidarToken(1)
def obtener_roles():
    respuesta: Respuesta =  rolControlador.mostrarTodosLosRoles()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appRoles.route('/roles/<int:rol_id>', methods=['GET'])
@ValidarToken(1)
def obtener_rol_por_id(rol_id):
    respuesta: Respuesta = rolControlador.mostrarRolPorId(rol_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appRoles.route('/roles/<int:rol_id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_rol(rol_id):
    payload = request.get_json()
    respuesta: Respuesta = rolControlador.actualizarRol(
        rol_id,
        payload.get('nombreRol')
    )
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appRoles.route('/roles/<int:rol_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_rol(rol_id):
    respuesta: Respuesta = rolControlador.borrarRol(rol_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appRoles.route('/roles', methods=['POST'])
@ValidarToken(1)
def crear_rol():
    try:
        payload = request.get_json()
        respuesta: Respuesta = rolControlador.InsertarNuevoRol(payload.get('nombreRol'))
        body = respuesta.to_dict()
        return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400
    except Exception as e:
        return jsonify({f"error": "Error interno del servidor {e}"}), 500