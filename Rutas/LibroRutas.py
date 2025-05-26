from flask import Blueprint, request, jsonify
from datetime import datetime
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.LibroControlador import LibroControlador

libroControlador = LibroControlador()

appLibros = Blueprint('libros', __name__)

def validar_fecha(fecha_str: str) -> bool:
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

@appLibros.route('/libros', methods=['POST'])
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


@appLibros.route('/libros', methods=['GET'])
def obtener_libros():
    print("entro")
    respuesta = libroControlador.mostrarTodos()
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 404



@appLibros.route('/libros/<int:libro_id>', methods=['GET'])
def obtener_libro_por_id(libro_id):
    respuesta = libroControlador.mostrarPorId(libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 404



@appLibros.route('/libros/<int:libro_id>', methods=['PUT'])
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

@appLibros.route('/libros/<int:libro_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_libro(libro_id):
    respuesta = libroControlador.borrarLibro(libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.get_estado() == "Operación Exitosa" else 400