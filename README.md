# CPSC 253 Project 1 Encryption Algorithm

- **key** = an 8-byte string (8 characters)

- **input**: text -> **output**: encrypted text of same length

- **N**: sum(ascii values of key's characters) modulo 8

# Example: 
plaintext = "hello there!"
key = "catmouse"

sequence = "ca" -> 11001010 -> 202

1. take the first two characters of the key (one hex byte) and convert it to a number 
2. sequentially go through the plaintext, and if the n array is true, invert the byte (wrap around)
3. Create N, which is the sum of the ASCII values of the key times 727 (a prime number) all modulo 8
4. 

