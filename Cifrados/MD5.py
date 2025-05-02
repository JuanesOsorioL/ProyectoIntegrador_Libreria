import os, binascii, hashlib

class MD5:

    def encrypt(self, password_plano: str)-> tuple:

        salt_bytes = os.urandom(16)
        salt   = binascii.hexlify(salt_bytes).decode()

        raw = salt + password_plano
        contrasena = hashlib.md5(raw.encode('utf-8')).hexdigest()
        salt = salt
        return contrasena,salt
    
    def verificar(self, contrasena: str, salt: str, hash_guardado: str) -> bool:
        raw = salt + contrasena
        hash_tmp = hashlib.md5(raw.encode('utf-8')).hexdigest()
        return hash_tmp == hash_guardado
