from src.file_io import *
from src.keygen import keygen

key = keygen()

encrypt_file("voyage.txt", "voyage_encrypted.txt", key)
decrypt_file("voyage_encrypted.txt", "voyage_decrypted.txt", key)

print(f'key: {key}')