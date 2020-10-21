# veracrypt installed

# siri kali

    https://www.2daygeek.com/sirikali-password-protect-encrypt-decrypt-folder-directory-linux/2/




# generate a 2048-bit RSA key and store it in key.txt
	
	openssl genrsa -out key.txt 2048

# encrypt "hello world" using the RSA key in key.txt
	
	echo "hello world" | openssl rsautl -inkey key.txt -encrypt >output.bin

# decrypt the message and output to stdout
	
	openssl rsautl -inkey key.txt -decrypt <output.bin


---

## Second method

If you have gpg installed, this is an industrial-strength encryption method.

	gpg --encrypt -r recipient@example.com >tempfile

Type data at the console and press Ctrl+D to end the text. This will give you encrypted data in tempfile. To decrypt:

	gpg --decrypt <tempfile

You will need the passphrase for recipient@example.com to decrypt the message.

---

## Third method - this methods seems to be outdated, but works with files

Encrypt and Decrypt File

To encrypt files with OpenSSL is as simple as encrypting messages. The only difference is that instead of the echo command we use the -in option with the actual file we would like to encrypt and -out option, which will instruct OpenSSL to store the encrypted file under a given name:
Warning: Ensure that the encrypted output file is given a different filename than the original plain input file. It is also recommended to do few encrypt/decrypt test runs on dummy data before encrypting important content.

	$ openssl enc -aes-256-cbc -in /etc/services -out services.dat

To decrypt back our services file use:

	$ openssl enc -aes-256-cbc -d -in services.dat > services.txt

	enter aes-256-cbc decryption password:
