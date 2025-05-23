from flask import Flask, request, jsonify
from Controlador.RolControlador import RolControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Dtos.Generico.Respuesta import Respuesta
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador
from datetime import datetime
from Controlador.CrearBDControlador import CrearBDControlador
from Cifrados.JWT import JWT
from Utilidades.ValidarToken import ValidarToken

jwt=JWT()
app = Flask(__name__)
usuarioSistemaControlador = UsuarioSistemaControlador()
rolControlador = RolControlador()
usuarioControlador=UsuarioControlador()

def validar_fecha(fecha_str: str) -> bool:
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

#crear BD
@app.route('/crear', methods=['GET'])
def crearBD():
    respuesta = CrearBDControlador.creartablasprocedimientos()
    payload = respuesta.to_dict()
    status_code = 200 if respuesta.get_estado() == "Operación Exitosa" else 500
    return jsonify(payload), status_code

#regitro
@app.route('/registro', methods=['POST'])
def registro():
    try:
        payload = request.get_json()
        usuario_respuesta:Respuesta = usuarioControlador.insertarUsuario(
            nombre=payload.get('nombre'),
            email=payload.get('email'),
            telefono=payload.get('telefono'),
            direccion=payload.get('direccion'),
            rol_id=payload.get('rolId'),
            nombre_usuario=payload.get('nombreUsuario'),
            contrasena=payload.get('contrasena')
        )
        body = usuario_respuesta.to_dict()
        #print("final",body)
        estado_http = 200 if usuario_respuesta.get_estado() == "Operación Exitosa" else 400
        return jsonify(body), estado_http

    except Exception as e:
        return jsonify({
            "estado": "Error",
            "mensaje": f"Excepción inesperada: {str(e)}",
            "resultado": []
        }), 500

#loguin
@app.route('/login', methods=['POST'])
def login():
    try:
        payload = request.get_json()
        respuesta: Respuesta = usuarioSistemaControlador.obtenerPorNombreUsuarioYContrasena(
            payload.get('nombreUsuario'),
            payload.get('contrasena')
        )
        body = respuesta.to_dict()
        return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 401
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500
    
#usuario
@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_usuario(usuario_id):
    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorId(usuario_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios', methods=['GET'])
@ValidarToken(1,2)
def lista_usuarios():
    respuesta: Respuesta =  usuarioControlador.mostrarTodosLosUsuarios()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios/email/<string:email>', methods=['GET'])
@ValidarToken(1,2)
def obtener_por_email(email):
    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorEmail(email)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios/rol/<int:rol_id>', methods=['GET'])
@ValidarToken(1,2)
def usuarios_por_rol(rol_id):
    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorRolId(rol_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
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

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def borrar_usuario(usuario_id):
    respuesta: Respuesta = usuarioControlador.borrarUsuario(usuario_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

# Rutas para usuarios del sistema

@app.route('/usuarios_sistema', methods=['GET'])
@ValidarToken(1)
def lista_usuarios_Sistema():
    respuesta: Respuesta =  usuarioSistemaControlador.listarUsuariosSistema()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios_sistema/<int:usuario_sistema_id>', methods=['GET'])
@ValidarToken(1)
def usuarios_Sistema_por_Id(usuario_sistema_id):
    respuesta: Respuesta =  usuarioSistemaControlador.obtenerUsuariosSistemaPorId(usuario_sistema_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios_sistema/por_username', methods=['POST'])
@ValidarToken(1)
def obtener_usuario_por_username():
    try:
        payload = request.get_json()
        respuesta: Respuesta = usuarioSistemaControlador.obtenerPorNombreUsuario(payload.get('nombreUsuario'),)
        body = respuesta.to_dict()
        return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/usuarios_sistema/<int:usuario_sistema_id>', methods=['PUT'])
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

@app.route('/usuarios_sistema/<int:usuario_sistema_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_usuario_sistema(usuario_sistema_id):
    respuesta: Respuesta = usuarioSistemaControlador.eliminarNombreUsuario(usuario_sistema_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

# Rol

@app.route('/roles', methods=['GET'])
@ValidarToken(1)
def obtener_roles():
    respuesta: Respuesta =  rolControlador.mostrarTodosLosRoles()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/roles/<int:rol_id>', methods=['GET'])
@ValidarToken(1)
def obtener_rol_por_id(rol_id):
    respuesta: Respuesta = rolControlador.mostrarRolPorId(rol_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/roles/<int:rol_id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_rol(rol_id):
    payload = request.get_json()
    respuesta: Respuesta = rolControlador.actualizarRol(
        rol_id,
        payload.get('nombreRol')
    )
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/roles/<int:rol_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_rol(rol_id):
    respuesta: Respuesta = rolControlador.borrarRol(rol_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/roles', methods=['POST'])
@ValidarToken(1)
def crear_rol():
    try:
        payload = request.get_json()
        respuesta: Respuesta = rolControlador.InsertarNuevoRol(payload.get('nombreRol'))
        body = respuesta.to_dict()
        return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400
    except Exception as e:
        return jsonify({f"error": "Error interno del servidor {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)


