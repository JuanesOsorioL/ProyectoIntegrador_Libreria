from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.DetallePrestamoControlador import DetallePrestamoControlador

detallePrestamoControlador = DetallePrestamoControlador()

appDetallesPrestamos = Blueprint('detallesPrestamos', __name__)

@appDetallesPrestamos.route('/detallesPrestamos', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalles_prestamo():
    respuesta = detallePrestamoControlador.mostrarTodosLosDetalles()
    return jsonify(respuesta.to_dict()), 200

@appDetallesPrestamos.route('/detallesPrestamos/<int:prestamo_id>/<int:libro_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalle_prestamo_id(prestamo_id, libro_id):
    respuesta = detallePrestamoControlador.mostrarDetallePorId(prestamo_id, libro_id)
    return jsonify(respuesta.to_dict()), 200

@appDetallesPrestamos.route('/detallesPrestamos', methods=['POST'])
@ValidarToken(1,2)
def crear_detalle_prestamo():
    payload = request.get_json()
    respuesta = detallePrestamoControlador.insertarDetalle(
        payload.get('prestamo_id'),
        payload.get('libro_id'),
        payload.get('cantidad')
    )
    return jsonify(respuesta.to_dict()), 200

@appDetallesPrestamos.route('/detallesPrestamos/<int:prestamo_id>/<int:libro_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_detalle_prestamo(prestamo_id, libro_id):
    payload = request.get_json()
    respuesta = detallePrestamoControlador.actualizarDetalle(prestamo_id, libro_id, payload.get('cantidad'))
    return jsonify(respuesta.to_dict()), 200

@appDetallesPrestamos.route('/detallesPrestamos/<int:prestamo_id>/<int:libro_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_detalle_prestamo(prestamo_id, libro_id):
    respuesta = detallePrestamoControlador.borrarDetalle(prestamo_id, libro_id)
    return jsonify(respuesta.to_dict()), 200
