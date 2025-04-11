from typing import Any

class Respuesta:
    estado: str
    msj: str
    resultado: Any

    def __init__(self, estado: str, msj: str, resultado: Any):
        self._estado = estado
        self._msj = msj
        self._resultado = resultado

    def __str__(self) -> str:
        return f"estado='{self._estado}', msj='{self._msj}', resultado={self._resultado}"