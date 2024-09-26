from random import choice

def is_valid_key(key: str):
    return key.isalnum() and len(key) == 64

def keygen():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet.upper() + '1234567890'
    key = ''
    for _ in range(64):
        key += choice(alphabet)
    return key

def keyfile_gen(output_filename: str):
    with open(output_filename, 'w') as output_file:
        output_file.write(keygen())
    print(f'key written to keyfile {output_filename}')