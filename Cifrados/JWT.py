from datetime import datetime, timedelta, timezone
import jwt

class JWT:

    SECRET = "tu_clave_super_secreta"
    ALGORIT="HS256"
    
    try:
        def cifrar(payload: dict, exp_horas: int = 2) -> str:
            payload_copy = payload.copy()
            payload_copy["exp"]  = datetime.now(timezone.utc) + timedelta(hours=exp_horas)
            return jwt.encode(payload_copy, JWT.SECRET, algorithm=JWT.ALGORIT)

        def decode(token: str) -> dict:
            return jwt.decode(token, JWT.SECRET, algorithms=[JWT.ALGORIT])

    except Exception as ex:
        print(ex)