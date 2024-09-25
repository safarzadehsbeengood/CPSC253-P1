import sys
import argparse
import src.encryption as enc
from src.file_io import decrypt_file, encrypt_file
from src.keygen import keygen, is_valid_key

def is_text_file(file: str):
    return file.endswith(".txt")

def file_encryption():
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
        
def main():
    parser = argparse.ArgumentParser(description="Encryption and Decryption for CPSC253 Project 1") 
    parser.add_argument('key', type=str, help="16-character alphanumeric key for encryption/decryption")
    parser.add_argument('-e', '--encrypt', action='store_true', help="encrypt the file")
    parser.add_argument('-d', '--decrypt', action='store_true', help="decrypt the file")
    parser.add_argument('input_file', type=str, help="path to an input file")
    parser.add_argument('output_file', type=str, help="path to an output file")
    
    args = parser.parse_args()
    
    # handle encrypt/decrypt flags
    if args.encrypt and args.decrypt:
        print("Error: cannot use both --decrypt and --encrypt")
        return
    if not (args.encrypt or args.decrypt):
        print("Error: you must specify either --encrypt or --decrypt")
        return
    if not args.key or not is_valid_key(args.key):
        print(f'error: {args.key} is not a valid key; please use a 16-character alphanumeric key')
        return
    if not (is_text_file(args.input_file) and is_text_file(args.output_file)):
        print("error: non-text file supplied to input or output.")
        return
    
    if args.encrypt:
        print(f'Encrypting {args.input_file}...')
        encrypt_file(args.input_file, args.output_file, args.key)
        print(f'Encrypted text written to {args.output_file}!')
    
    if args.decrypt:
       print(f'Decrypting {args.input_file}...')
       decrypt_file(args.input_file, args.output_file, args.key)
       print(f'Decrypted text written to {args.output_file}!') 
            
if __name__ == "__main__":
    main()
            