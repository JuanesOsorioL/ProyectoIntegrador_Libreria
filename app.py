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
usuarioControlador=UsuarioControlador()


def validar_fecha(fecha_str: str) -> bool:
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


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
        print("Error en /login:", str(e))
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







"""

    estructura para validar si el rol es 3 para que no busque el de todos sino solo el 

    @app.route('/usuarios/<int:usuario_id>', methods=['GET'])
@ValidarToken(1, 2, 3)  # Admin, empleado y cliente
def obtener_usuario(usuario_id):
    payload = request.user_payload
    rol = payload.get("rol")
    usuario_actual = payload.get("usuario_id")

    # Si es cliente (rol 3), solo puede consultar su propio perfil
    if rol == 3 and usuario_actual != usuario_id:
        return jsonify({"error": "No tienes permiso para ver este usuario"}), 403

    respuesta: Respuesta = usuarioControlador.mostrarUsuarioPorId(usuario_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

def ValidarToken(*roles_permitidos):
    def decorator(func):
        @wraps(func)
        def Token(*args, **kwargs):
            token_header = request.headers.get("Token")
            if not token_header or not token_header.startswith("Bearer "):
                return jsonify({"error": "Token requerido"}), 401

            try:
                token = token_header.split()[1]
                payload = jwt.decode(token, JWT.SECRET, algorithms=[JWT.ALGORIT])
                rol = payload.get("rol")

                if rol not in roles_permitidos:
                    return jsonify({"error": "Rol no autorizado"}), 403

                # Guardar payload para que el endpoint lo use
                request.user_payload = payload

            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expirado"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Token inválido"}), 403

            return func(*args, **kwargs)
        return Token
    return decorator

payload = {
    "sub": nombre_usuario,
    "rol": 3,
    "usuario_id": 42
}


"""
