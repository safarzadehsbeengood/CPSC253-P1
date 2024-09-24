from random import choice

def keygen():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet.upper() + '1234567890'
    key = ''
    for _ in range(16):
        key += choice(alphabet)
    return key