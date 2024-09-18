from .encryption import encrypt, decrypt

def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            pt = file.read()
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encrypt(pt, key))
    except FileNotFoundError:
        print(f'(encryption) - Error: {input_file} not found!')

def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            ct = file.read()
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decrypt(ct, key))
    except FileNotFoundError:
        print(f"(decryption) - Error: {input_file} not found!")
