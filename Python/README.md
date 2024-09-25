
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

## Example Usage

### Encryption Example
Encrypting a file `helloworld.txt` to a file `helloworld_encrypted.txt` using a keyfile `key`:

```bash
python3 main.py -e key helloworld.txt helloworld_encrypted.txt
```

### Decryption Example
Decrypting a file `helloworld_encrypted.txt` to a file `helloworld_decrypted.txt` using a keyfile `key`:

```bash
python3 main.py -d key helloworld_encrypted.txt helloworld_decrypted.txt
```