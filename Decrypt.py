import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import Encrypt


def unpad(text):
    last_character = text[len(text) - 1:]
    bytes_to_remove = ord(last_character)
    return text[:-bytes_to_remove]


def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def decrypt_text(cipher_text, key):
    private_key = get_private_key(key)
    enc = base64.b64encode(cipher_text)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


def decrypt_file():
    pass
