from flask import Blueprint, request, jsonify
from datetime import datetime
from Dtos.Generico.Respuesta import Respuesta
from Utilidades.ValidarToken import ValidarToken
from Controlador.DevolucionControlador import DevolucionControlador

devolucionControlador = DevolucionControlador()

appDevoluciones = Blueprint('devoluciones', __name__)

def validar_fecha(fecha_str: str) -> bool:
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False
    
@appDevoluciones.route('/devoluciones', methods=['POST'])
@ValidarToken(1,2)
def crear_devolucion():
    payload = request.get_json()
    fecha = payload.get('fecha_real_devolucion')
    if not validar_fecha(fecha):
        return jsonify({"estado": "Error", "msj": "Fecha inválida", "resultado": []}), 400

    respuesta: Respuesta = devolucionControlador.insertarDevolucion(
        fecha,
        payload.get('prestamo_id'),
        payload.get('estado_libro'),
        payload.get('observaciones')
    )
    body = respuesta.to_dict()
    return jsonify(body), 201 if respuesta.get_estado() == "Operación Exitosa" else 400


@appDevoluciones.route('/devoluciones', methods=['GET'])
@ValidarToken(1,2)
def obtener_devoluciones():
    respuesta: Respuesta = devolucionControlador.mostrarTodasLasDevoluciones()
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404

@appDevoluciones.route('/devoluciones/<int:devolucion_id>', methods=['GET'])
@ValidarToken(1,2)
def obtener_devolucion_por_id(devolucion_id):
    respuesta: Respuesta = devolucionControlador.mostrarDevolucionPorId(devolucion_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 404



@appDevoluciones.route('/devoluciones/<int:devolucion_id>', methods=['PUT'])
@ValidarToken(1,2)
def actualizar_devolucion(devolucion_id):
    payload = request.get_json()
    fecha = payload.get('fecha_real_devolucion')
    if not validar_fecha(fecha):
        return jsonify({"estado": "Error", "msj": "Fecha inválida", "resultado": []}), 400

    respuesta: Respuesta = devolucionControlador.actualizarDevolucion(
        devolucion_id,
        payload.get('prestamo_id'),
        fecha,
        payload.get('estado_libro'),
        payload.get('observaciones')
    )
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400

@appDevoluciones.route('/devoluciones/<int:devolucion_id>', methods=['DELETE'])
@ValidarToken(1,2)
def eliminar_devolucion(devolucion_id):
    respuesta: Respuesta = devolucionControlador.borrarDevolucion(devolucion_id)
    body = respuesta.to_dict()
    return jsonify(body), 200 if respuesta.get_estado() == "Operación Exitosa" else 400