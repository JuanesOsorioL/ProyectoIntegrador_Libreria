
from datetime import datetime
from flask import Flask, request, jsonify

from Utilidades.ValidarToken import ValidarToken
from Cifrados.JWT import JWT
from Dtos.Generico.Respuesta import Respuesta

from Controlador.CrearBDControlador import CrearBDControlador
from Controlador.RolControlador import RolControlador
from Controlador.AutorControlador import AutorControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador
from Controlador.CategoriaControlador import CategoriaControlador
from Controlador.EditorialControlador import EditorialControlador
from Controlador.LibroAutorControlador import LibroAutorControlador
from Controlador.LibroCategoriaControlador import LibroCategoriaControlador
from Controlador.DevolucionControlador import DevolucionControlador
from Controlador.LibroControlador import LibroControlador
from Controlador.VentaControlador import VentaControlador
from Controlador.DetalleVentaControlador import DetalleVentaControlador
from Controlador.PrestamoControlador import PrestamoControlador
from Controlador.DetallePrestamoControlador import DetallePrestamoControlador

jwt=JWT()
app = Flask(__name__)

usuarioSistemaControlador = UsuarioSistemaControlador()
rolControlador = RolControlador()
usuarioControlador=UsuarioControlador()
autorControlador=AutorControlador()
categoriaControlador=CategoriaControlador()
editorialControlador=EditorialControlador()
libroAutorControlador=LibroAutorControlador()
libroCategoriaControlador=LibroCategoriaControlador()
devolucionControlador = DevolucionControlador()
libroControlador = LibroControlador()
ventaControlador = VentaControlador()
detalleVentaControlador = DetalleVentaControlador()
prestamoControlador = PrestamoControlador()
detallePrestamoControlador = DetallePrestamoControlador()


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



#Autor

@app.route('/autores', methods=['POST'])
@ValidarToken(1,2)
def crear_autor():
    payload = request.get_json()
    nombre = payload.get('nombre')
    nacionalidad = payload.get('nacionalidad')
    respuesta: Respuesta = autorControlador.insertarAutor(nombre, nacionalidad)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/autores', methods=['GET'])
@ValidarToken(1,2)
def obtener_autores():
    respuesta: Respuesta = autorControlador.mostrarTodosLosAutores()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/autores/<int:autor_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_autor_por_id(autor_id):
    respuesta: Respuesta = autorControlador.mostrarAutorPorId(autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/autores/<int:autor_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_autor(autor_id):
    payload = request.get_json()
    nombre = payload.get('nombre')
    nacionalidad = payload.get('nacionalidad')
    respuesta: Respuesta = autorControlador.actualizarAutor(autor_id, nombre, nacionalidad)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/autores/<int:autor_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_autor(autor_id):
    respuesta: Respuesta = autorControlador.borrarAutor(autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

# Categoría

@app.route('/categorias', methods=['POST'])
@ValidarToken(1,2)
def crear_categoria():
    payload = request.get_json()
    nombre = payload.get('nombre')
    respuesta: Respuesta = categoriaControlador.insertarCategoria(nombre)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/categorias', methods=['GET'])
@ValidarToken(1,2)
def obtener_categorias():
    respuesta: Respuesta = categoriaControlador.mostrarTodasLasCategorias()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/categorias/<int:categoria_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_categoria_por_id(categoria_id):
    respuesta: Respuesta = categoriaControlador.mostrarCategoriaPorId(categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/categorias/<int:categoria_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_categoria(categoria_id):
    payload = request.get_json()
    nombre = payload.get('nombre')
    respuesta: Respuesta = categoriaControlador.actualizarCategoria(categoria_id, nombre)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/categorias/<int:categoria_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_categoria(categoria_id):
    respuesta: Respuesta = categoriaControlador.borrarCategoria(categoria_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400


# Editorial

@app.route('/editoriales', methods=['POST'])
@ValidarToken(1,2)
def crear_editorial():
    payload = request.get_json()
    respuesta: Respuesta = editorialControlador.insertarEditorial(payload.get('nombre'), payload.get('pais'))
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400


@app.route('/editoriales', methods=['GET'])
@ValidarToken(1,2)
def obtener_editoriales():
    respuesta: Respuesta = editorialControlador.mostrarTodasLasEditoriales()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/editoriales/<int:editorial_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_editorial_por_id(editorial_id):
    respuesta: Respuesta = editorialControlador.mostrarEditorialPorId(editorial_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@app.route('/editoriales/<int:editorial_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_editorial(editorial_id):
    payload = request.get_json()
    nombre = payload.get('nombre')
    pais = payload.get('pais')
    respuesta: Respuesta = editorialControlador.actualizarEditorial(editorial_id, nombre, pais)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/editoriales/<int:editorial_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_editorial(editorial_id):
    respuesta: Respuesta = editorialControlador.borrarEditorial(editorial_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

# DEVOLUCIONES

@app.route('/devoluciones', methods=['GET'])
def obtener_devoluciones():
    respuesta = devolucionControlador.mostrarTodasLasDevoluciones()
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/devoluciones/<int:devolucion_id>', methods=['GET'])
def obtener_devolucion_por_id(devolucion_id):
    respuesta = devolucionControlador.mostrarDevolucionPorId(devolucion_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/devoluciones', methods=['POST'])
@ValidarToken(1,2)
def crear_devolucion():
    payload = request.get_json()
    fecha = payload.get('fecha_real_devolucion')
    if not validar_fecha(fecha):
        return jsonify({"estado": "Error", "msj": "Fecha inválida", "resultado": []}), 400

    respuesta = devolucionControlador.insertarDevolucion(
        fecha,
        payload.get('estado_libro'),
        payload.get('observaciones')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/devoluciones/<int:devolucion_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_devolucion(devolucion_id):
    payload = request.get_json()
    fecha = payload.get('fecha_real_devolucion')
    if not validar_fecha(fecha):
        return jsonify({"estado": "Error", "msj": "Fecha inválida", "resultado": []}), 400

    respuesta = devolucionControlador.actualizarDevolucion(
        devolucion_id,
        fecha,
        payload.get('estado_libro'),
        payload.get('observaciones')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/devoluciones/<int:devolucion_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_devolucion(devolucion_id):
    respuesta = devolucionControlador.borrarDevolucion(devolucion_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

# LIBROS

@app.route('/libros', methods=['GET'])
def obtener_libros():
    respuesta = libroControlador.mostrarTodos()
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/libros/<int:libro_id>', methods=['GET'])
def obtener_libro_por_id(libro_id):
    respuesta = libroControlador.mostrarPorId(libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@app.route('/libros', methods=['POST'])
@ValidarToken(1,2)
def crear_libro():
    payload = request.get_json()
    respuesta = libroControlador.insertarLibro(
        payload.get('titulo'),
        payload.get('isbn'),
        payload.get('descripcion'),
        payload.get('anio_publicacion'),
        payload.get('formato'),
        payload.get('editorial_id'),
        payload.get('precio'),
        payload.get('stock')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/libros/<int:libro_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_libro(libro_id):
    payload = request.get_json()
    respuesta = libroControlador.actualizarLibro(
        libro_id,
        payload.get('titulo'),
        payload.get('isbn'),
        payload.get('descripcion'),
        payload.get('anio_publicacion'),
        payload.get('formato'),
        payload.get('editorial_id'),
        payload.get('precio'),
        payload.get('stock')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/libros/<int:libro_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_libro(libro_id):
    respuesta = libroControlador.borrarLibro(libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400


# VENTAS

@app.route('/ventas', methods=['GET'])
@ValidarToken(1,2)
def obtener_ventas():
    respuesta = ventaControlador.mostrarTodasLasVentas()
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/ventas/<int:venta_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_venta_por_id(venta_id):
    respuesta = ventaControlador.mostrarVentaPorId(venta_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/ventas', methods=['POST'])
@ValidarToken(1,2)
def crear_venta():
    payload = request.get_json()
    respuesta = ventaControlador.insertarVenta(
        payload.get('cliente_id'),
        payload.get('empleado_id'),
        payload.get('total')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@app.route('/ventas/<int:venta_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_venta(venta_id):
    payload = request.get_json()
    respuesta = ventaControlador.actualizarVenta(
        venta_id,
        payload.get('cliente_id'),
        payload.get('empleado_id'),
        payload.get('fecha'),
        payload.get('total')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@app.route('/ventas/<int:venta_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_venta(venta_id):
    respuesta = ventaControlador.borrarVenta(venta_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400


# Detalle Ventas

@app.route('/detallesVentas', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalles():
    respuesta = detalleVentaControlador.mostrarTodosLosDetalles()
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/detallesVentas/<int:venta_id>/<int:libro_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalle_por_id(venta_id, libro_id):
    respuesta = detalleVentaControlador.mostrarDetallePorId(venta_id, libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/detallesVentas/venta/<int:venta_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalles_por_venta(venta_id):
    respuesta = detalleVentaControlador.mostrarDetallesDeUnaVenta(venta_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/detallesVentas', methods=['POST'])
@ValidarToken(1,2)
def crear_detalle():
    payload = request.get_json()
    respuesta = detalleVentaControlador.insertarDetalle(
        payload.get('venta_id'),
        payload.get('libro_id'),
        payload.get('cantidad'),
        payload.get('precio_unitario')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@app.route('/detallesVentas/<int:venta_id>/<int:libro_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_detalle(venta_id, libro_id):
    payload = request.get_json()
    respuesta = detalleVentaControlador.actualizarDetalle(
        venta_id,
        libro_id,
        payload.get('cantidad'),
        payload.get('precio_unitario')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@app.route('/detallesVentas/<int:venta_id>/<int:libro_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_detalle(venta_id, libro_id):
    respuesta = detalleVentaControlador.borrarDetalle(venta_id, libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400


# Prestamo

@app.route('/prestamos', methods=['GET'])
def obtener_prestamos():
    respuesta = prestamoControlador.mostrarTodosLosPrestamos()
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/prestamos/<int:prestamo_id>', methods=['GET'])
def obtener_prestamo_por_id(prestamo_id):
    respuesta = prestamoControlador.mostrarPrestamoPorId(prestamo_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@app.route('/prestamos', methods=['POST'])
def crear_prestamo():
    payload = request.get_json()
    respuesta = prestamoControlador.insertarPrestamo(
        payload.get('cliente_id'),
        payload.get('empleado_id'),
        payload.get('fecha_prestamo'),
        payload.get('fecha_devolucion'),
        payload.get('estado')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@app.route('/prestamos/<int:prestamo_id>', methods=['PUT'])
def actualizar_prestamo(prestamo_id):
    payload = request.get_json()
    respuesta = prestamoControlador.actualizarPrestamo(
        prestamo_id,
        payload.get('cliente_id'),
        payload.get('empleado_id'),
        payload.get('fecha_prestamo'),
        payload.get('fecha_devolucion'),
        payload.get('estado')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@app.route('/prestamos/<int:prestamo_id>', methods=['DELETE'])
def eliminar_prestamo(prestamo_id):
    respuesta = prestamoControlador.borrarPrestamo(prestamo_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400


# Detalle Prestamo

@app.route('/detallesPrestamos', methods=['GET'])
def obtener_detalles_prestamo():
    respuesta = detallePrestamoControlador.mostrarTodosLosDetalles()
    return jsonify(respuesta.to_dict()), 200

@app.route('/detallesPrestamos/<int:prestamo_id>/<int:libro_id>', methods=['GET'])
def obtener_detalle_prestamo_id(prestamo_id, libro_id):
    respuesta = detallePrestamoControlador.mostrarDetallePorId(prestamo_id, libro_id)
    return jsonify(respuesta.to_dict()), 200

@app.route('/detallesPrestamos', methods=['POST'])
def crear_detalle_prestamo():
    payload = request.get_json()
    respuesta = detallePrestamoControlador.insertarDetalle(
        payload.get('prestamo_id'),
        payload.get('libro_id'),
        payload.get('cantidad')
    )
    return jsonify(respuesta.to_dict()), 200

@app.route('/detallesPrestamos/<int:prestamo_id>/<int:libro_id>', methods=['PUT'])
def actualizar_detalle_prestamo(prestamo_id, libro_id):
    payload = request.get_json()
    respuesta = detallePrestamoControlador.actualizarDetalle(prestamo_id, libro_id, payload.get('cantidad'))
    return jsonify(respuesta.to_dict()), 200

@app.route('/detallesPrestamos/<int:prestamo_id>/<int:libro_id>', methods=['DELETE'])
def eliminar_detalle_prestamo(prestamo_id, libro_id):
    respuesta = detallePrestamoControlador.borrarDetalle(prestamo_id, libro_id)
    return jsonify(respuesta.to_dict()), 200























# Libro-Autor (relación) no verificada

@app.route('/libros-autores', methods=['POST'])
@ValidarToken(1)
def crear_libro_autor():
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    autor_id = payload.get('autor_id')
    respuesta: Respuesta = libroAutorControlador.insertarLibroAutor(libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400

@app.route('/libros-autores', methods=['GET'])
@ValidarToken(1)
def obtener_libros_autores():
    respuesta: Respuesta = libroAutorControlador.mostrarTodosLosLibroAutor()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@app.route('/libros-autores/<int:libro_id>/<int:autor_id>', methods=['GET'])
@ValidarToken(1)
def obtener_libro_autor_por_id(libro_id, autor_id):
    respuesta: Respuesta = libroAutorControlador.mostrarLibroAutorPorId(libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404


@app.route('/libros-autores/<int:libro_id>/<int:autor_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_libro_autor(libro_id, autor_id):
    respuesta: Respuesta = libroAutorControlador.borrarLibroAutor(libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400


@app.route('/libros-autores/<int:id>', methods=['PUT'])
@ValidarToken(1)
def actualizar_libro_autor(id):
    payload = request.get_json()
    libro_id = payload.get('libro_id')
    autor_id = payload.get('autor_id')
    respuesta: Respuesta = libroAutorControlador.actualizarLibroAutor(id, libro_id, autor_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

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

