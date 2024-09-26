# CPSC253 Project 1 (Encryption Algorithm)
### Author: Ryan Safarzadeh

---

Required:
- Python 3.6 or higher

This program allows you to encrypt and decrypt plaintext files using a 64-character alphanumeric key.

## Features
- **Encrypt plaintext** using a 64-character alphanumeric key.
- **Decrypt ciphertext** back into the original plaintext using the same key.
- **Generate a key** by writing to a file or by printing to the terminal.

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

### Interactive
To use the interactive script, you can run the program with no arguments:
```bash
python3 main.py
```

### CLI Tool
To encrypt, decrypt, or generate a key in one command, you can pass in arguments:
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

---

# Algorithm

The following section provides a pseudocode explanation for an encryption and decryption system that uses a 64-byte alphanumeric key. 

---

## Constants

- **`KEY_SIZE = 64`**: The size of the key is 64 bytes.
- **`CR_PLACEHOLDER = chr(255)`**: Placeholder for carriage returns (extended ASCII character 255).
- **`SPECIAL_DELIMITER = chr(254)`**: Delimiter to separate special characters from the encrypted text (extended ASCII character 254).

---

## `encrypt(pt: str, key: str)`

**Purpose**: Encrypts the plaintext (`pt`) using a 64-character alphanumeric key.

### Inputs:
- `pt`: The plaintext string to be encrypted.
- `key`: A 64-character alphanumeric string.

### Outputs:
- Encrypted text with special characters appended at the end.

### Steps:
1. **Validate the key**:
   - If the key is not 64 characters long or not alphanumeric, exit with an error message.

2. **Initialize variables**:
   - `keyIndex`: Set to `0` to track the current position in the key.
   - `res`: Empty string to store the result of the encrypted text.
   - `special_chars`: Empty string to store special characters (like carriage returns).

3. **Loop through each character `c` in the plaintext**:
   - **Check if the current key character is even**:
     - If even:
       - Encrypt by inverting the bits of `c` and applying modulo 128.
       - If the result is a **carriage return** (ASCII `13`):
         - Append the `CR_PLACEHOLDER` to `res`.
         - Add `c` to `special_chars`.
       - Otherwise, append the encrypted character to `res`.
   - **If the current key character is odd**:
     - Encrypt by adding the ASCII value of `c` and the key character, then apply modulo 128.
     - If the result is a **carriage return** (ASCII `13`):
       - Append the `CR_PLACEHOLDER` to `res`.
       - Add `c` to `special_chars`.
     - Otherwise, append the encrypted character to `res`.

4. **Update the key index**:
   - Increment `keyIndex`.
   - If `keyIndex` exceeds `KEY_SIZE - 1`, wrap it back to `0`.

5. **Return**:
   - Concatenate the encrypted text (`res`) with the `SPECIAL_DELIMITER` and the string of `special_chars`.

---

## `decrypt(ct: str, key: str)`

**Purpose**: Decrypts the ciphertext (`ct`) using the same 64-character alphanumeric key used for encryption.

### Inputs:
- `ct`: The ciphertext string to be decrypted.
- `key`: A 64-character alphanumeric string.

### Outputs:
- Decrypted plaintext string.

### Steps:
1. **Initialize variables**:
   - `res`: Empty string to store the decrypted result.
   - `special_chars`: Extract the portion of the ciphertext after the `SPECIAL_DELIMITER` and convert it to a list.
   - `ct`: Remove the `SPECIAL_DELIMITER` and the special characters from the ciphertext.
   - `keyIndex`: Set to the index at the last encrypted character, calculated by `len(ct) % len(key) - 1`.

2. **Loop through the ciphertext in reverse**:
   - For each character `c` in `ct`:
     - **If the character is a `CR_PLACEHOLDER`**:
       - Pop the last character from `special_chars` and append it to `res`.
     - **Otherwise**:
       - **Check if the current key character is even**:
         - If even, decrypt by inverting the bits of the character and applying modulo 128.
       - **If the current key character is odd**:
         - Subtract the ASCII value of the key character from the character `c`.
         - If the result is negative, wrap it by adding 128.

3. **Update the key index**:
   - Decrement `keyIndex`.
   - If `keyIndex` is less than `0`, wrap it back to the length of the key.

4. **Return**:
   - Reverse the string `res` and return it to get the original decrypted text.

---

<em>**Note**: This documentation was written with the help of AI, but was thoroughly reviewed.</em>
