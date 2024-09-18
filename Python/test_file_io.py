from src.file_io import *

key = "1234abcd5678efgh"

encrypt_file("voyage.txt", "voyage_encrypted.txt", key)
decrypt_file("voyage_encrypted.txt", "voyage_decrypted.txt", key)
