from typing import Any

class ResultadoRepositorio:
    def __init__(self, codigo: int, objecto: Any = None, mensaje: str = None):
        self.codigo = codigo
        self.objecto = objecto
        self.mensaje = mensaje