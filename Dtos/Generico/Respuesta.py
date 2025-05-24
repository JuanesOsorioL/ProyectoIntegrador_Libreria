from typing import Any

class Respuesta:
    estado: str
    msj: str
    resultado: Any
    token: str

    def __init__(self, estado: str, msj: str, resultado: Any, token: str = None):
        self._estado = estado
        self._msj = msj
        self._resultado = resultado
        self._token=token

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

    def get_token(self) -> str:
        return self._token


    @property
    def token(self):
        return self._token
    
    @property
    def estado(self):
        return self._estado

    @property
    def msj(self):
        return self._msj

    @property
    def resultado(self):
        return self._resultado

    def to_dict(self) -> dict:
        base= {
            "estado":    self.estado,
            "mensaje":   self.msj,
            "resultado": self.resultado
        }
        if self.token and isinstance(self.token, str):
            base["token"] = self.token
        return base