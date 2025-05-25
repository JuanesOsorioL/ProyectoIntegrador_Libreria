from datetime import datetime
from flask import Flask, request, jsonify


from Dtos.Generico.Respuesta import Respuesta
from Cifrados.JWT import JWT
from Utilidades.ValidarToken import ValidarToken

from Controlador.CrearBDControlador import CrearBDControlador
from Controlador.RolControlador import RolControlador
from Controlador.AutorControlador import AutorControlador
from Controlador.UsuarioControlador import UsuarioControlador
from Controlador.UsuarioSistemaControlador import UsuarioSistemaControlador
from Controlador.CategoriaControlador import CategoriaControlador
from Controlador.EditorialControlador import EditorialControlador
from Controlador.LibroAutorControlador import LibroAutorControlador
from Controlador.LibroCategoriaControlador import LibroCategoriaControlador
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
    nombre = payload.get('nombre')
    pais = payload.get('pais')
    respuesta: Respuesta = editorialControlador.insertarEditorial(nombre, pais)
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


