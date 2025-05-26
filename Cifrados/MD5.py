import os, binascii, hashlib

class MD5:
    
    @staticmethod
    def encrypt(password_plano: str)-> tuple:
        # 1) Generar salt aleatorio de 16 bytes
        salt_bytes = os.urandom(16)
        salt   = binascii.hexlify(salt_bytes).decode()
        # 2) Concatenar salt + password y hashear
        raw = salt + password_plano
        contrasena = hashlib.md5(raw.encode('utf-8')).hexdigest()
        return contrasena,salt
    
    @staticmethod
    def verificar(contrasena: str, salt: str, hash_guardado: str) -> bool:
        #Verifica que md5(salt + password) == hashed.
        raw = salt + contrasena
        hash_tmp = hashlib.md5(raw.encode('utf-8')).hexdigest()
        return hash_tmp == hash_guardado