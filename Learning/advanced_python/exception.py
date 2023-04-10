try:
	open('text.txt','r')
except IOError:
	print("le fichier n'existe pas")
