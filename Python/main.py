import sys
from src.file_io import decrypt_file, encrypt_file
        
if __name__ == "__main__":
    choice = None
    print("Welcome! Would you like to:\n\t1. Encrypt\n\t2. Decrypt\n\tq: Cancel\n")
    while choice is None:
        choice = input("> ")
        if choice == '1' or choice == '2' or choice == 'q':
            break
        print("Invalid input, please try again.")
    
    if choice != 'q':
        input_file = input("Enter an input file: ")
        output_file = input("Enter an output file: ")
        key = input("Enter a 16-character key (alphanumeric characters only): ")
        while len(key) != 16 and not key.isalnum():
            key = input("Invalid format, try again: ")
        if choice == '1':
            encrypt_file(input_file, output_file, key)
        else:
            decrypt_file(input_file, output_file, key)
    else:
        sys.exit()
            