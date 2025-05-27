from datetime import datetime
from flask import Flask, request, jsonify
from Cifrados.JWT import JWT
from Dtos.Generico.Respuesta import Respuesta

from Controlador.CrearBDControlador import CrearBDControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador

from Rutas.UsuarioRutas import appUsuarios
from Rutas.UsuarioSistemaRutas import appUsuariosSistema
from Rutas.RolRutas import appRoles
from Rutas.AutorRutas import appAutores
from Rutas.CategoriaRutas import appCategorias
from Rutas.EditorialRutas import appEditorial
from Rutas.DevolucionesRutas import appDevoluciones
from Rutas.LibroRutas import appLibros
from Rutas.PrestamoRutas import appPrestamos
from Rutas.VentaRutas import appVentas
from Rutas.DetalleVentaRutas import appDetallesVentas
from Rutas.DetallePrestamo import appDetallesPrestamos
from Rutas.LibroAutorRutas import appLibroAutores
from Rutas.LibroCategorias import appLibroCategoria

jwt=JWT()
app = Flask(__name__)

usuarioSistemaControlador = UsuarioSistemaControlador()
usuarioControlador=UsuarioControlador()

app.register_blueprint(appUsuarios)
app.register_blueprint(appUsuariosSistema)
app.register_blueprint(appRoles)
app.register_blueprint(appAutores)
app.register_blueprint(appCategorias)
app.register_blueprint(appEditorial)
app.register_blueprint(appDevoluciones)
app.register_blueprint(appLibros)
app.register_blueprint(appPrestamos)
app.register_blueprint(appVentas)
app.register_blueprint(appDetallesVentas)
app.register_blueprint(appDetallesPrestamos)
app.register_blueprint(appLibroAutores)
app.register_blueprint(appLibroCategoria)


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
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)