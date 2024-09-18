KEY_SIZE = 16

def encrypt(pt: str, key: str):
    keyIndex = 0
    res = ''

    for c in pt:
        # if even, invert the bits of the byte
        even = ord(key[keyIndex]) % 2 == 0
        if even:
            res += chr((ord(c) ^ 0x7f) % 128)
            print(f'[encrypt] * {c} -> {res[-1]} INVERT')

        # otherwise, add the ascii value of the key's current char and make that the new character
        else:
            res += chr((ord(c) + ord(key[keyIndex])) % 128)
            print(f'[encrypt] * {c} -> {res[-1]} ADD')

        # increment the key index and wrap if it exceeds the key length
        keyIndex += 1
        if keyIndex > KEY_SIZE-1:
            keyIndex = 0
    return res

def decrypt(ct: str, key: str):
    keyIndex = len(ct) % len(key) - 1
    res = ''
    # reverse the ciphertext
    for i in range(len(ct)-1, -1, -1):
        c = ct[i]
        even = ord(key[keyIndex]) % 2 == 0
        if even:
            res += chr((ord(c) ^ 0x7f) % 128)
        else:
            newCharIndex = ord(c) - ord(key[keyIndex])
            if newCharIndex < 0:
                newCharIndex += 128
            res += chr(newCharIndex)
        keyIndex -= 1
        if keyIndex < 0:
            keyIndex = len(key)-1
    return res[::-1]