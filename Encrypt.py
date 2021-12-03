import hashlib
from Crypto.Cipher import AES


def pad(text):
    number_of_bytes_to_pad = AES.block_size - len(text) % AES.block_size
    ascii_string = str(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string

    padded = text + padding_str

    return padded


def encrypt_text(text, key):
    key = hashlib.sha256(key.encode()).digest()
    pad(text)

    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(text)

    return cipher_text


def encrypt_file(file, key):
    pass
