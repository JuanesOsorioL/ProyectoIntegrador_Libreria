from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador

usuarioSistemaControlador = UsuarioSistemaControlador()

appUsuariosSistema = Blueprint('usuarios_sistema', __name__)

@appUsuariosSistema.route('/usuarios_sistema', methods=['GET'])
@ValidarToken(1)
def lista_usuarios_Sistema():
    respuesta: Respuesta =  usuarioSistemaControlador.listarUsuariosSistema()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuariosSistema.route('/usuarios_sistema/<int:usuario_sistema_id>', methods=['GET'])
@ValidarToken(1)
def usuarios_Sistema_por_Id(usuario_sistema_id):
    respuesta: Respuesta =  usuarioSistemaControlador.obtenerUsuariosSistemaPorId(usuario_sistema_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuariosSistema.route('/usuarios_sistema/por_username', methods=['POST'])
@ValidarToken(1)
def obtener_usuario_por_username():
    try:
        payload = request.get_json()
        respuesta: Respuesta = usuarioSistemaControlador.obtenerPorNombreUsuario(payload.get('nombreUsuario'),)
        body = respuesta.to_dict()
        return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@appUsuariosSistema.route('/usuarios_sistema/<int:usuario_sistema_id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_usuario_sistema(usuario_sistema_id):
    payload = request.get_json()
    respuesta: Respuesta = usuarioSistemaControlador.actualizarUsuarioSistemaPorId(
        usuario_sistema_id,
        payload.get('nombreUsuario'),
        payload.get('contrasena')
    )
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appUsuariosSistema.route('/usuarios_sistema/<int:usuario_sistema_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_usuario_sistema(usuario_sistema_id):
    respuesta: Respuesta = usuarioSistemaControlador.eliminarNombreUsuario(usuario_sistema_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400