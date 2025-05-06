from Servicio.UsuarioSistemaServicio import UsuarioSistemaServicio
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO
from Dtos.Generico.Respuesta import Respuesta

import json
import flask

app = flask.Flask(__name__)
usuarioSistemaServicio = UsuarioSistemaServicio()

class UsuarioSistemaControlador:
    """
        @app.route('/usuarioSistema', methods=['POST'])
        def insertar(entrada):
            datos = parse_json_param(entrada)
            resp = controlador.insertar(
                datos['usuario_id'],
                datos['nombre_usuario'],
                datos['contrasena']
            )
            return flask.jsonify(resp)

    """





    def insertar(self, usuario_id: int, nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None,usuario_id,nombre_usuario,contrasena, None)
        return usuarioSistemaServicio.insertar(dto)
    
    def obtenerPorNombreUsuarioYContrasena(self, nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None, None, nombre_usuario, contrasena, None)
        return usuarioSistemaServicio.obtenerPorUsernameYContrasena(dto)


###
    def listar(self) -> Respuesta:
        return usuarioSistemaServicio.listar()

    def obtenerPorId(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None, None)
        return usuarioSistemaServicio.obtener_por_id(dto)

    def obtenerPorNombreUsuario(self, nombre_usuario: str) -> Respuesta:
        dto = UsuarioSistemaDTO(None, None, nombre_usuario, None, None)
        return usuarioSistemaServicio.obtenerPorUsername(dto)

    def actualizar(self, id: int, usuario_id: int, nombre_usuario: str, contrasena: str) -> Respuesta:
        dto = UsuarioSistemaDTO(id,usuario_id,nombre_usuario,contrasena, None)
        return usuarioSistemaServicio.actualizar(dto)

    def eliminar(self, id: int) -> Respuesta:
        dto = UsuarioSistemaDTO(id, None, None, None, None)
        return usuarioSistemaServicio.eliminar(dto)