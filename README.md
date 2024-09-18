# CPSC 253 Project 1 Encryption Algorithm

- **key** = a 16-byte string (16 characters)

- **input**: text -> **output**: encrypted text of same length

# Overview: 
### Encryption
1. Keep a keyIndex that will keep track of the current character in the key
2. sequentially go through the plaintext, and if the keyIndex's ASCII value is even, invert the bits of that character's ASCII value; otherwise, add the keyIndex's ASCII value to it and modulo 128, then add that ASCII value to the result string 

### Decryption
1. Start the keyIndex the length of the ciphertext modulo the length of the key, since that's where it would've left off
2. Sequentially move backwards through the ciphertext and decode the character based on the keyIndex character
3. If the keyIndex character's ASCII value is even, invert the bits again; else subtract the keyIndex character's ascii value from it and add 128 if it's negative

### Key complexity
The key is 16 alphanumeric characters, so brute-forcing would yield 62^16 possibilities.
