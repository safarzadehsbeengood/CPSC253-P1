from encryption import encrypt, decrypt

message = """
The Moon above so high and bright,  
Guides my way through darkest night.  
With silver beams, it lights the sky,  
A gentle watchful, silent eye.  

The winds may howl, the stars may fade,  
But Moonlight's grace will never jade.  
Through storm and calm, through joy and pain,  
The Moon will rise and shine again.
"""

key = "1234abcd5678efgh"

print(f'Message: {message}')
print(f'Key: {key}')

ct = encrypt(message, key)
print(f'Encrypted: {ct}')

pt = decrypt(ct, key)
print(f'Decrypted: {pt}')
