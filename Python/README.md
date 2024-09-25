
# Python Encryption/Decryption Program

This program allows you to encrypt and decrypt text using a 64-character alphanumeric key.

## Features
- **Encrypt plaintext** using a 64-character alphanumeric key.
- **Decrypt ciphertext** back into the original plaintext using the same key.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/safarzadehsbeengood/CPSC253-P1.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd CPSC253-P1
   ```

## Usage

Once you've installed the program, you can run it to either encrypt or decrypt text.
```bash
usage: main.py [-h] [-g] [-k <file>] [-e] [-d] [-i <file>] [-o <file>]

Encryption and Decryption for CPSC253 Project 1

options:
  -h, --help            show this help message and exit
  -g, --keygen          flag to use the key generator (if output_file is given, will be written there)
  -k <file>, --key <file>
                        path to keyfile
  -e, --encrypt         encrypt the file
  -d, --decrypt         decrypt the file
  -i <file>, --input_file <file>
                        path to an input file
  -o <file>, --output_file <file>
                        path to an output file
```
## Example Usage

### Encryption Example
Encrypting a file `helloworld.txt` to a file `helloworld_encrypted.txt` using a keyfile `key`:

```bash
python3 main.py -k key -e -i helloworld.txt -o helloworld_encrypted.txt
```

### Decryption Example
Decrypting a file `helloworld_encrypted.txt` to a file `helloworld_decrypted.txt` using a keyfile `key`:

```bash
python3 main.py -k key -d -i helloworld_encrypted.txt -o helloworld_decrypted.txt
```