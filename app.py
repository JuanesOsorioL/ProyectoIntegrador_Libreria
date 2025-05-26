from datetime import datetime
from flask import Flask, request, jsonify

from Utilidades.ValidarToken import ValidarToken
from Cifrados.JWT import JWT
from Dtos.Generico.Respuesta import Respuesta

from Controlador.CrearBDControlador import CrearBDControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador

from Controlador.LibroCategoriaControlador import LibroCategoriaControlador








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


jwt=JWT()
app = Flask(__name__)

usuarioSistemaControlador = UsuarioSistemaControlador()
usuarioControlador=UsuarioControlador()

libroCategoriaControlador=LibroCategoriaControlador()



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


# Rutas para usuarios del sistema



# Rol




#Autor



# Categoría


# Editorial



# DEVOLUCIONES


# LIBROS


# VENTAS


# Detalle Ventas



# Prestamo



# Detalle Prestamo























# Libro-Autor (relación) no verificada

# Libro-Categoría (relación)

@app.route('/libros-categorias', methods=['GET'])
@ValidarToken(1)
def obtener_libros_categorias():
    respuesta: Respuesta = libroCategoriaControlador.mostrarTodosLosLibroCategoria()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@app.route('/libros-categorias/<int:libro_id>/<int:categoria_id>', methods=['GET'])
@ValidarToken(1)
def obtener_libro_categoria_por_id(libro_id, categoria_id):
    respuesta: Respuesta = libroCategoriaControlador.mostrarLibroCategoriaPorId(libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@app.route('/libros-categorias/<int:libro_id>/<int:categoria_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_libro_categoria(libro_id, categoria_id):
    respuesta: Respuesta = libroCategoriaControlador.borrarLibroCategoria(libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400


@app.route('/libros-categorias', methods=['POST'])
@ValidarToken(1)
def crear_libro_categoria():
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    categoria_id = payload.get('categoria_id')
    respuesta: Respuesta = libroCategoriaControlador.insertarLibroCategoria(libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/libros-categorias/<int:id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_libro_categoria(id):
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    categoria_id = payload.get('categoria_id')
    respuesta: Respuesta = libroCategoriaControlador.actualizarLibroCategoria(id, libro_id, categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400






if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

