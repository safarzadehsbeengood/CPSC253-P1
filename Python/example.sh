# An example script which will generate a keyfile, use it to encrypt a text file, and then decrypt it back into plaintext

python3 main.py -g -o example_key
sleep 1
python3 main.py -k example_key -e -i asyoulik.txt -o example_encrypted.txt
sleep 1
python3 main.py -k example_key -d -i example_encrypted.txt -o example_decrypted.txt
sleep 1
diff asyoulik.txt example_decrypted.txt
