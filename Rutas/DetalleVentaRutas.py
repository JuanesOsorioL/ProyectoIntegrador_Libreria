from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.DetalleVentaControlador import DetalleVentaControlador

detalleVentaControlador = DetalleVentaControlador()

appDetallesVentas = Blueprint('detallesVentas', __name__)

@appDetallesVentas.route('/detallesVentas', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalles():
    respuesta = detalleVentaControlador.mostrarTodosLosDetalles()
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@appDetallesVentas.route('/detallesVentas/<int:venta_id>/<int:libro_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalle_por_id(venta_id, libro_id):
    respuesta = detalleVentaControlador.mostrarDetallePorId(venta_id, libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@appDetallesVentas.route('/detallesVentas/venta/<int:venta_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_detalles_por_venta(venta_id):
    respuesta = detalleVentaControlador.mostrarDetallesDeUnaVenta(venta_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@appDetallesVentas.route('/detallesVentas', methods=['POST'])
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

@appDetallesVentas.route('/detallesVentas/<int:venta_id>/<int:libro_id>', methods=['PUT'])
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

@appDetallesVentas.route('/detallesVentas/<int:venta_id>/<int:libro_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_detalle(venta_id, libro_id):
    respuesta = detalleVentaControlador.borrarDetalle(venta_id, libro_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400