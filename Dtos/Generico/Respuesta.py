from typing import Any

class Respuesta:
    estado: str
    msj: str
    resultado: Any

    def __init__(self, estado: str, msj: str, resultado: Any):
        self._estado = estado
        self._msj = msj
        self._resultado = resultado

    def get_estado(self) -> str:
        return self._estado

    def set_estado(self, value: str) -> None:
        self._estado = value

    def get_msj(self) -> str:
        return self._msj

    def set_msj(self, value: str) -> None:
        self._msj = value

    def get_resultado(self) -> Any:
        return self._resultado

    def set_resultado(self, value: Any) -> None:
        self._resultado = value

    def __str__(self) -> str:
        return f"estado='{self._estado}', msj='{self._msj}', resultado={self._resultado}"