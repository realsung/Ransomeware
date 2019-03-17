import os
from Crypto.Cipher import AES
from Crypto import Random
from sys import stdout
from Get_data import get_keys
from Crypto.Hash import SHA256

def getkey(password):
	hasher = SHA256.new(password)
	return hasher.digest()

def write(word):
	stdout.write(word+"                                         \r")
	stdout.flush()
	return True

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = str(filename)+".unifox"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)
	try:
		with open(filename, 'rb') as infile:
			with open(outputFile, 'wb') as outfile:
				outfile.write(filesize.encode('utf-8'))
				outfile.write(IV)

				while True:
					chunk = infile.read(chunksize)

					if len(chunk) == 0:
						break 
					elif len(chunk) % 16 != 0:
						chunk += b' ' * (16 - (len(chunk) % 16))

					outfile.write(encryptor.encrypt(chunk))
	except IOError:
		pass