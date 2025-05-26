from flask import Blueprint, request, jsonify
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.VentaControlador import VentaControlador

ventaControlador = VentaControlador()

appVentas = Blueprint('ventas', __name__)

@appVentas.route('/ventas', methods=['GET'])
@ValidarToken(1,2)
def obtener_ventas():
    respuesta = ventaControlador.mostrarTodasLasVentas()
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@appVentas.route('/ventas/<int:venta_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_venta_por_id(venta_id):
    respuesta = ventaControlador.mostrarVentaPorId(venta_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 404

@appVentas.route('/ventas', methods=['POST'])
@ValidarToken(1,2)
def crear_venta():
    payload = request.get_json()
    respuesta = ventaControlador.insertarVenta(
        payload.get('cliente_id'),
        payload.get('empleado_id'),
        payload.get('total')
    )
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400

@appVentas.route('/ventas/<int:venta_id>', methods=['PUT'])
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

@appVentas.route('/ventas/<int:venta_id>', methods=['DELETE'])
@ValidarToken(1)
def eliminar_venta(venta_id):
    respuesta = ventaControlador.borrarVenta(venta_id)
    return jsonify(respuesta.to_dict()), 200 if respuesta.estado == "Operación Exitosa" else 400
