from src.file_io import decrypt_file, encrypt_file, get_key_from_file
from src.keygen import keygen, keyfile_gen
from src.utils import *
from os.path import isfile
        
def main():
    if not args_passed():
        choice = None
        print("Welcome! Would you like to:\n\n 1. Encrypt\n 2. Decrypt\n q: Cancel\n")
        while choice is None:
            choice = input("> ")
            if choice == '1' or choice == '2' or choice == 'q':
                break
            print("Invalid input, please try again.")
            choice = None
    
        if choice != 'q':
            input_file = input("Enter an input file: ")
            output_file = input("Enter an output file: ")
            key = input("Enter the name of a keyfile or enter 'keygen' for a random key: ")
            while not isfile(key) and key != 'q' and key != 'keygen':
                key = input("Invalid format, try again (q to cancel): ")
            if key == 'q':
                return
            if key == 'keygen':
                key = keygen()
                print("> [using random key]")
            else:
                key = get_key_from_file(key)
            if choice == '1':
                encrypt_file(input_file, output_file, key)
                print(f'{input_file} encrypted to {output_file} with key {key}.')
            else:
                decrypt_file(input_file, output_file, key)
                print(f'{input_file} decrypted to {output_file} with key {key}.')
        else:
            return
    else:
        parser = argparse_gen()
        args = parser.parse_args()
        if not verify_args(args):
            parser.print_help()
            return

        if args.keygen:
            if args.output_file:
                keyfile_gen(args.output_file)
            else:
                print(f'key: {keygen()}')
            return
        
        key = get_key_from_file(args.key)
        
        if args.encrypt:
            print(f'Encrypting {args.input_file}...')
            encrypt_file(args.input_file, args.output_file, key)
            print(f'Encrypted text written to {args.output_file}!')
        
        elif args.decrypt:
            print(f'Decrypting {args.input_file}...')
            decrypt_file(args.input_file, args.output_file, key)
            print(f'Decrypted text written to {args.output_file}!') 
            
if __name__ == "__main__":
    main()
            