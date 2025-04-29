import os
from Crypto.Cipher import AES

class AES_GCM:

    def cifrar(self) -> int:
        return os.urandom(32)

    def cifrar(self, texto: str) -> dict:
        key = AES_GCM.cifrar()
        aes = AES.new(key, AES.MODE_GCM)
        c, tag = aes.encrypt_and_digest(str.encode(texto))
        return {"ciphertext":c, "nonce":aes.nonce, "tag":tag, "key":key}
 

    def descifrar(self,  data: dict) -> str:
        aes = AES.new(data["key"], AES.MODE_GCM, data["tag"])
        return aes.decrypt_and_verify(data["ciphertext"], data["tag"]).decode()