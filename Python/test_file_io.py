from src.file_io import *
from src.keygen import keygen

key = keygen()

encrypt_file("txt/voyage.txt", "txt/voyage_encrypted.txt", key)
decrypt_file("txt/voyage_encrypted.txt", "txt/voyage_decrypted.txt", key)

print(f'key: {key}')
