import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2


def pad(text):
    number_of_bytes_to_pad = AES.block_size - len(text) % AES.block_size
    ascii_string = str(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string

    padded = text + padding_str

    return padded


def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def encrypt_text(text, key):
    private_key = get_private_key(key)
    text = pad(text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(text))


def encrypt_file(file, key):
    pass
