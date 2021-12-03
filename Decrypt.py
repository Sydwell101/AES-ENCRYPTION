from Crypto.Cipher import AES
import Encrypt


def unpad(text):
    last_character = text[len(text) - 1:]
    bytes_to_remove = ord(last_character)
    return text[:-bytes_to_remove]


def decrypt_text(cipher_text, key):
    key = key.decode('UTF-8')
    cipher_text = Encrypt.encrypt_text(cipher_text, key)
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_data = cipher.decrypt(cipher_text)
    decrypted_data = decrypted_data.decode('UTF-8')
    unpadded = unpad(decrypted_data)
    decrypted_data = decrypted_data[:unpadded]

    return decrypted_data


def decrypt_file():
    pass
