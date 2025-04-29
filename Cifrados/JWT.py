from datetime import datetime, timedelta, timezone
import jwt

class JWT:

    SECRET = "tu_clave_super_secreta"
    ALGORIT="HS256"
    
    try:
        def cifrar(self, payload: dict, exp_horas: int = 2) -> str:
            payload_copy = payload.copy()
            payload_copy["exp"]  = datetime.now(timezone.utc) + timedelta(hours=exp_horas)
            return jwt.encode(payload_copy, self.SECRET, algorithm=self.ALGORIT)

        def decode(self, token: str) -> dict:
            return jwt.decode(token, self.SECRET, algorithms=[self.ALGORIT])

    except Exception as ex:
        print(ex)