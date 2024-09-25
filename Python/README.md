
# Python Encryption/Decryption Program

This program allows you to encrypt and decrypt text using a 16-character alphanumeric key. The system handles special characters, such as carriage returns, by appending them to the end of the ciphertext.

## Features
- **Encrypt plaintext** using a 16-character alphanumeric key.
- **Decrypt ciphertext** back into the original plaintext using the same key.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [License](#license)

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

### Encrypting/Decrypting Text
#### To use the interactive cli, run the following command:

```bash
python3 main.py
```

#### To encrypt/decrypt a file from the command line:
```bash
python3 main.py ["encrypt"/"decrypt"] <input_file> <output_file>
```

## Example

### Encryption Example
Encrypting the text "Hello, World!" using the key "A1B2C3D4E5F6G7H8":

```bash
python3 main.py encrypt "Hello, World!" "A1B2C3D4E5F6G7H8"
```

Output:
```
Encrypted text: ƃџүҙҟӨұӂңңҡƶчʺҠøϸч
```

### Decryption Example
Decrypting the encrypted text using the same key:

```bash
python3 main.py decrypt "ƃџүҙҟӨұӂңңҡƶчʺҠøϸч" "A1B2C3D4E5F6G7H8"
```

Output:
```
Decrypted text: Hello, World!
```

## Troubleshooting

1. **Invalid Key Error**:
   If you receive the following error message:
   ```bash
   ERR: Invalid key! Please use a 16-character alphanumeric key.
   ```
   - Ensure your key is exactly 16 characters long.
   - Only alphanumeric characters (letters and digits) are allowed.

2. **Carriage Return Handling**:
   If your plaintext or ciphertext contains carriage returns (e.g., from pressing "Enter"), the program will store those as special characters and append them to the ciphertext.

3. **File Not Found Error**:
   Ensure you're running the commands in the correct directory and the file `main.py` exists.

4. **Python Version**:
   Make sure you're using Python 3.6 or above. You can check your Python version with:
   ```bash
   python3 --version
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
