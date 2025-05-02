import hmac
import hashlib
from Crypto.Cipher import AES
from typing import Tuple, Optional

class CryptoConfig:

    AES_KEY = b"0123456789abcdef0123456789abcdef"
    HMAC_KEY = b"fedcba9876543210fedcba9876543210"

class AESHMAC:

    def encrypt(username: str) -> Tuple[bytes, bytes, bytes]:
        cipher = AES.new(CryptoConfig.AES_KEY, AES.MODE_GCM)
        ct, tag = cipher.encrypt_and_digest(username.encode("utf-8"))
        return ct, cipher.nonce, tag


    def decrypt(ciphertext: bytes, nonce: bytes, auth_tag: bytes) -> str:
        cipher = AES.new(CryptoConfig.AES_KEY, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, auth_tag)
        return plaintext.decode("utf-8")

    def hmac(username: str) -> str:
        hm = hmac.new(CryptoConfig.HMAC_KEY, username.encode("utf-8"), hashlib.sha256)
        return hm.hexdigest()