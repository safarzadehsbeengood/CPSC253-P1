from .encryption import encrypt, decrypt
from .keygen import is_valid_key

def get_key_from_file(filename: str):
    try:
        with open(filename, 'r') as keyfile:
            key = keyfile.read()
            return key if is_valid_key(key) else False
    except FileNotFoundError:
        print(f"(get_key_from_file) Error: file {keyfile} not found!")
        return False

def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            pt = file.read()
        with open(output_file, 'w') as file:
            file.write(encrypt(pt, key))
        return True
    except FileNotFoundError:
        print(f'(encryption) - Error: {input_file} not found!')
        return False

def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            ct = file.read()
        with open(output_file, 'w') as file:
            file.write(decrypt(ct, key))
        return True
    except FileNotFoundError:
        print(f"(decryption) - Error: {input_file} not found!")
        return False
