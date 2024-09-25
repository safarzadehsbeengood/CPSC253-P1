import sys
from src.file_io import decrypt_file, encrypt_file
from src.keygen import keygen
        
if __name__ == "__main__":
    choice = None
    print("Welcome! Would you like to:\n\t1. Encrypt\n\t2. Decrypt\n\tq: Cancel")
    while choice is None:
        choice = input("> ")
        if choice == '1' or choice == '2' or choice == 'q':
            break
        print("Invalid input, please try again.")
        choice = None
    
    if choice != 'q':
        input_file = input("Enter an input file: ")
        output_file = input("Enter an output file: ")
        key = input("Enter a 16-character key (alphanumeric characters only) or 'keygen' for a random key: ")
        while len(key) != 16 and not key.isalnum() and key != 'q' and key != 'keygen':
            key = input("Invalid format, try again (q to cancel): ")
        if key == 'keygen':
            key = keygen()
        if choice == '1':
            encrypt_file(input_file, output_file, key)
            print(f'{input_file} encrypted to {output_file} with key {key}.')
        else:
            decrypt_file(input_file, output_file, key)
            print(f'{input_file} decrypted to {output_file} with key {key}.')
    else:
        sys.exit()
            