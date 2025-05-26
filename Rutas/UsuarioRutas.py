from flask import Blueprint, request, jsonify
from datetime import datetime
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.UsuarioControlador import UsuarioControlador

usuarioControlador=UsuarioControlador()

appUsuarios = Blueprint('usuarios', __name__)

def validar_fecha(fecha_str: str) -> bool:
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

@appUsuarios.route('/usuarios/<int:usuario_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_usuario(usuario_id):
    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorId(usuario_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuarios.route('/usuarios', methods=['GET'])
@ValidarToken(1,2)
def lista_usuarios():
    respuesta: Respuesta =  usuarioControlador.mostrarTodosLosUsuarios()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuarios.route('/usuarios/email/<string:email>', methods=['GET'])
@ValidarToken(1,2)
def obtener_por_email(email):
    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorEmail(email)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuarios.route('/usuarios/rol/<int:rol_id>', methods=['GET'])
@ValidarToken(1,2)
def usuarios_por_rol(rol_id):
    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorRolId(rol_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuarios.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    payload = request.get_json()
    fecha_input = payload.get('fechaRegistro')

    if not validar_fecha(fecha_input):
        return jsonify({
            "estado":  "Error",
            "mensaje": "Fecha inválida: debe tener formato YYYY-MM-DD",
            "resultado": []
        }), 400
    
    respuesta: Respuesta = usuarioControlador.actualizarUsuario(
        usuario_id,
        payload.get('nombre'),
        payload.get('email'),
        payload.get('telefono'),
        payload.get('direccion'),
        fecha_input,
        payload.get('rolId')
    )
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appUsuarios.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def borrar_usuario(usuario_id):
    respuesta: Respuesta = usuarioControlador.borrarUsuario(usuario_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404