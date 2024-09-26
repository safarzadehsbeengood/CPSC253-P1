# An example script which will generate a keyfile, use it to encrypt a text file, and then decrypt it back into plaintext

python3 main.py -g -o example/example_key
sleep 1
python3 main.py -k example/example_key -e -i example/asyoulik.txt -o example/example_encrypted.txt
sleep 1
python3 main.py -k example/example_key -d -i example/example_encrypted.txt -o example/example_decrypted.txt
sleep 1
diff example/asyoulik.txt example/example_decrypted.txt
