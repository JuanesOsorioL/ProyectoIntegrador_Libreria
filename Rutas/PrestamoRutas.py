from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.PrestamoControlador import PrestamoControlador

prestamoControlador = PrestamoControlador()

appPrestamos = Blueprint('prestamos', __name__)

@appPrestamos.route('/prestamos', methods=['POST'])
@ValidarToken(1,2)
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




@appPrestamos.route('/prestamos', methods=['GET'])
@ValidarToken(1,2)
def obtener_prestamos():
    respuesta = prestamoControlador.mostrarTodosLosPrestamos()
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@appPrestamos.route('/prestamos/<int:prestamo_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_prestamo_por_id(prestamo_id):
    respuesta = prestamoControlador.mostrarPrestamoPorId(prestamo_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404


@appPrestamos.route('/prestamos/<int:prestamo_id>', methods=['PUT'])
@ValidarToken(1,2)
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

@appPrestamos.route('/prestamos/<int:prestamo_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_prestamo(prestamo_id):
    respuesta = prestamoControlador.borrarPrestamo(prestamo_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400