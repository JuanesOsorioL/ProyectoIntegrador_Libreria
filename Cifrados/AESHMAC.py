import msgpack
import hmac
import hashlib
from Crypto.Cipher import AES
from typing import Tuple

class CryptoConfig:

    AES_KEY = b"0123456789abcdef0123456789abcdef"
    HMAC_KEY = b"fedcba9876543210fedcba9876543210"

class AESHMAC:

    
    def encriptar(self, username: str) -> Tuple[bytes, bytes, bytes]:
        cipher = AES.new(CryptoConfig.AES_KEY, AES.MODE_GCM)
        ct, tag = cipher.encrypt_and_digest(username.encode("utf-8"))
        return ct, cipher.nonce, tag

    def desencriptar(self, ciphertext: bytes, nonce: bytes, auth_tag: bytes) -> str:
        cipher = AES.new(CryptoConfig.AES_KEY, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, auth_tag)
        return plaintext.decode("utf-8")

    def hmac(self, username: str) -> str:
        hm = hmac.new(CryptoConfig.HMAC_KEY, username.encode("utf-8"), hashlib.sha256)
        return hm.hexdigest()
    
    def sellar(self, plaintext: str) -> Tuple[bytes, str]:
        ct, nonce, tag = self.encriptar(plaintext)
        hmac_value    = self.hmac(plaintext)
        packed        = msgpack.packb({
            "nonce": nonce,
            "tag":   tag,
            "ct":    ct
        })
        return packed, hmac_value
    
    def desellarlo(self, packed: bytes) -> str:
        # raw=False para que las claves msgpack vengan como str en lugar de bytes
        data = msgpack.unpackb(packed, raw=False)

        nonce = data["nonce"]
        tag   = data["tag"]
        ct    = data["ct"]

        return self.desencriptar(ct, nonce, tag)