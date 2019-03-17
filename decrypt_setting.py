from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from sys import stdout

def write(word):
	stdout.write(word+"                                         \r")
	stdout.flush()
	return True

def getkey(key):
	key = SHA256.new(key) #key.encode('utf-8')
	return key.digest()

def decrypt(key, filename):
	buffersize = 64 * 1024
	outputfile = filename.split('.unifox')[0]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputfile, 'wb') as outfile:
			while True:
				buf = infile.read(buffersize)

				if len(buf) == 0:
					break

				outfile.write(decryptor.decrypt(buf))
			outfile.truncate(filesize)
