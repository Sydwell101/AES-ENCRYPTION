import Encrypt
import Decrypt


def main():
    plain_text = input('Enter your data to be encrypted: ')
    key = input('Enter your secret key: ')

    print('Encrypting Data...')

    encrypted_data = Encrypt.encrypt_text(plain_text, key)
    print(f'Encrypted data= {encrypted_data}')

    print('Done.')

    print('Decrypting Data...')
    decrypted_data = Decrypt.decrypt_text(encrypted_data, key)
    print(f'Decrypted data= {decrypted_data}')


if __name__ == '__main__':
    main()
