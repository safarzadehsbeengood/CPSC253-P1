import argparse
import sys

# verify text files
def is_text_file(file: str):
    return file.endswith(".txt")

# check if any arguments were passed
def args_passed():
    return len(sys.argv) > 1

# verify flags from CLI
def verify_args(args):
    # handle flags
    if args.keygen and (args.encrypt or args.decrypt):
        print("error: must either use keygen or encrypt/decrypt function, not both")
        return False
    if args.encrypt and args.decrypt:
        print("error: cannot use both --decrypt and --encrypt")
        return False
    if not args.keygen and not (args.encrypt or args.decrypt):
        print("error: you must specify either --encrypt or --decrypt")
        return False
    if not args.keygen and not (is_text_file(args.input_file) and is_text_file(args.output_file)):
        print("error: non-text file supplied to input or output")
        return False
    return True


# argument parser for CLI
def argparse_gen():
    parser = argparse.ArgumentParser(description="Encryption and Decryption for CPSC253 Project 1")
    parser.add_argument('-g', '--keygen', action='store_true', help="flag to use the key generator (if output_file is given, will be written there)")
    parser.add_argument('-k', '--key', metavar="<file>", type=str, help="path to keyfile")
    parser.add_argument('-e', '--encrypt', action='store_true', help="encrypt the file")
    parser.add_argument('-d', '--decrypt', action='store_true', help="decrypt the file")
    parser.add_argument('-i', '--input_file', metavar='<file>', type=str, required=False, help="path to an input file")
    parser.add_argument('-o', '--output_file', metavar='<file>', type=str, required=False, help="path to an output file")

    return parser