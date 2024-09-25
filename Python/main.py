from src.file_io import decrypt_file, encrypt_file, get_key_from_file
from src.keygen import keygen, keyfile_gen
from src.utils import *
        
def main():
    args = argparse_gen()
    if not verify_args(args):
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
            