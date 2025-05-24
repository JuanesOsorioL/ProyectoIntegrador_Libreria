import jwt
from functools import wraps
from flask import request, jsonify
from Cifrados.JWT import JWT

def ValidarToken(*roles_permitidos):
    def decorator(func):
        @wraps(func)
        def Token(*args, **kwargs):
            token_header = request.headers.get("Token")
            if not token_header or not token_header.startswith("Bearer "):
                return jsonify({"error": "Token requerido"}), 401

            try:
                token = token_header.split()[1]
                payload = jwt.decode(token, JWT.SECRET, algorithms=[JWT.ALGORIT])
                rol = payload.get("rol")

                if rol not in roles_permitidos:
                    return jsonify({"error": "Rol no autorizado"}), 403

                # Opcional: guardar el usuario para acceder desde el endpoint
                #request.user_payload = payload

            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expirado"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Token inválido"}), 403

            return func(*args, **kwargs)
        return Token
    return decorator