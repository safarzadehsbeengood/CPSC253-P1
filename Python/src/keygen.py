from random import choice

def is_valid_key(key: str):
    return key.isalnum() and len(key) == 16

def keygen():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet.upper() + '1234567890'
    key = ''
    for _ in range(16):
        key += choice(alphabet)
    return key