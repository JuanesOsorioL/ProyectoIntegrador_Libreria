from flask import Flask, request, jsonify
from Controlador.RolControlador import RolControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Dtos.Generico.Respuesta import Respuesta
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador
from datetime import datetime
from Controlador.CrearBDControlador import CrearBDControlador
from Cifrados.JWT import JWT

jwt=JWT()
app = Flask(__name__)
#regitro
@app.route('/registro', methods=['POST'])
def registro():
    try:
        payload = request.get_json()

        usuario_respuesta:Respuesta = UsuarioControlador.insertarUsuario(
            nombre=payload.get('nombre'),
            email=payload.get('email'),
            telefono=payload.get('telefono'),
            direccion=payload.get('direccion'),
            rol_id=payload.get('rolId'),
            nombre_usuario=payload.get('nombreUsuario'),
            contrasena=payload.get('contrasena')
        )
        body = usuario_respuesta.to_dict()
        print("final",body)
        estado_http = 200 if usuario_respuesta.get_estado() == "Operación Exitosa" else 400
        return jsonify(body), estado_http

    except Exception as e:
        return jsonify({
            "estado": "Error",
            "mensaje": f"Excepción inesperada: {str(e)}",
            "resultado": []
        }), 500



















def validar_fecha(fecha_str: str) -> bool:
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False
#usuario

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    resp = UsuarioControlador.mostrarUsuarioPorId(usuario_id)
    return jsonify(resp.to_dict()), 200 if resp.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios', methods=['GET'])
def lista_usuarios():
    resp = UsuarioControlador.mostrarTodosLosUsuarios()
    return jsonify(resp.to_dict()), 200

@app.route('/usuarios/email/<string:email>', methods=['GET'])
def obtener_por_email(email):
    resp = UsuarioControlador.mostrarUsuarioPorEmail(email)
    return jsonify(resp.to_dict()), 200 if resp.get_estado() == "Operación Exitosa" else 404

@app.route('/usuarios/rol/<int:rol_id>', methods=['GET'])
def usuarios_por_rol(rol_id):
    resp = UsuarioControlador.mostrarUsuarioPorRolId(rol_id)
    return jsonify(resp.to_dict()), 200 if resp.get_estado() == "Operación Exitosa" else 404

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
    
    resp = UsuarioControlador.actualizarUsuario(
        usuario_id,
        payload.get('nombre'),
        payload.get('email'),
        payload.get('telefono'),
        payload.get('direccion'),
        fecha_input,
        payload.get('rolId')
    )
    return jsonify(resp.to_dict()), 200 if resp.get_estado() == "Operación Exitosa" else 400

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def borrar_usuario(usuario_id):
    resp = UsuarioControlador.borrarUsuario(usuario_id)
    return jsonify(resp.to_dict()), 200 if resp.get_estado() == "Operación Exitosa" else 400

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    payload = request.get_json()
    fecha_input = payload.get('fechaRegistro')

    if not validar_fecha(fecha_input):
        return jsonify({
            "estado":  "Error",
            "mensaje": "Fecha inválida: debe tener formato YYYY-MM-DD",
            "resultado": []
        }), 400
    
    resp = UsuarioControlador.insertarUsuario(
        payload.get('nombre'),
        payload.get('email'),
        payload.get('telefono'),
        payload.get('direccion'),
        fecha_input,
        payload.get('rolId')
    )
    return jsonify(resp.to_dict()), 200 if resp.get_estado() == "Operación Exitosa" else 400


#usuario sistema







"""

# Rutas para usuarios
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    payload = request.get_json()
    resp = UsuarioControlador.insertarUsuario(
        payload.get('nombre'),
        payload.get('email'),
        payload.get('telefono'),
        payload.get('direccion'),
        payload.get('fecha_registro'),
        payload.get('rol_id')
    )
    return jsonify(vars(resp)), 201 if resp.mensaje == "Operación Exitosa" else 400

    

# Rutas para usuarios














# Rutas para usuarios del sistema (JWT)
@app.route('/usuarios-sistema', methods=['POST'])
def crear_usuario_sistema():
    payload = request.get_json()
    resp = usuario_sis_ctrl.insertar(
        payload.get('usuario_id'),
        payload.get('nombre_usuario'),
        payload.get('contrasena')
    )
    return jsonify(vars(resp)), 201 if resp.mensaje == "Operación Exitosa" else 400

@app.route('/login', methods=['POST'])
def login_usuario_sistema():
    payload = request.get_json()
    resp = usuario_sis_ctrl.obtenerPorNombreUsuarioYContrasena(
        payload.get('nombre_usuario'),
        payload.get('contrasena')
    )
    return jsonify(vars(resp)), 200 if resp.mensaje == "Operación Exitosa" else 401














"""











    







@app.route('/crear', methods=['GET'])
def crearBD():
    respuesta = CrearBDControlador.creartablasprocedimientos()
    payload = respuesta.to_dict()
    status_code = 200 if respuesta.get_estado() == "Operación Exitosa" else 500
    return jsonify(payload), status_code


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)