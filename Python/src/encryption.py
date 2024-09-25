KEY_SIZE = 64                   # # of bytes in the key
CR_PLACEHOLDER = chr(255)       # extended ascii character we'll use to account for special characters (when the encrypted character is a carriage return)
SPECIAL_DELIMITER = chr(254)    # the delimiter we'll use for appending special characters to the end of the encrypted text

from sys import exit, argv

def encrypt(pt: str, key: str):
    '''
    Will convert plaintext to a ciphertext using a 64-byte alphanumeric key.
    '''
    keyIndex = 0
    res = ''
    special_chars = ''

    for c in pt:
        even = ord(key[keyIndex]) % 2 == 0                          # check if the ascii value of the current key character is even
        if even:
            ec = chr((ord(c) ^ 0x7f) % 128)                         # the even case for encrypting a character (invert the bits and modulo 128)
            
            # carriage return case -> add the placeholder and save this character for later
            if ord(ec) == 13:
                res += CR_PLACEHOLDER
                special_chars += c
            # normal case -> add this character to the encrypted text
            else: 
                res += ec
        # if odd
        else:
            ec = chr((ord(c) + ord(key[keyIndex])) % 128)           # the odd case for encrypting a character (adding the current key character's ascii value and modulo 128)
            
            # carriage return case
            if ord(ec) == 13:
                res += CR_PLACEHOLDER
                special_chars += c
            # normal case
            else: 
                res += ec

        # increment the key index and wrap if it exceeds the key length
        keyIndex += 1
        if keyIndex > KEY_SIZE-1:
            keyIndex = 0
    return res + SPECIAL_DELIMITER + special_chars                  # return the encrypted text with the special characters appended at the end

def decrypt(ct: str, key: str):
    res = ''                                                        # the resulting decrypted text
    special_chars = list(ct.split(SPECIAL_DELIMITER)[-1])           # grab the special characters and turn them into a list
    ct = ct.split(SPECIAL_DELIMITER)[0]                             # separate the actual ciphertext from the special characters
    keyIndex = len(ct) % len(key) - 1                               # the key index at the last encrypted character is the length of the ciphertext modulo the length of the key
    
    # reverse through the ciphertext
    for i in range(len(ct)-1, -1, -1):
        c = ct[i]                                                   # grab this character
        if ord(c) == 255:                                           # if it's a placeholder,
            res += special_chars.pop()                              # pop off the last special character put it here
        else:                                                       # otherwise,
            even = ord(key[keyIndex]) % 2 == 0                      # check whether the current key's character is even or odd
            if even:                                                # if it's even,
                res += chr((ord(c) ^ 0x7f) % 128)                   # invert the bits of the ascii value and modulo 128
            else:                                                   # otherwise it's odd,
                newCharIndex = ord(c) - ord(key[keyIndex])          # so subtract the current key character's ascii value from it and wrap to the end in case it's negative
                if newCharIndex < 0:                                
                    newCharIndex += 128
                res += chr(newCharIndex)
        keyIndex -= 1                                               # decrement the key index and wrap around if necessary
        if keyIndex < 0:
            keyIndex = len(key)-1
    return res[::-1]                                                # return the result's reverse since we moved through backwards