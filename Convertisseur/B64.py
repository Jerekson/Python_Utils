#!/usr/bin/env python
import base64
#PYTHON 2 ONLY

choix = input("Encode ou Decode ? \n")

if choix == "encode" or choix == "Encode":
	pass
elif choix == "decode" or choix == "Decode":
	# texte : QmlsbHlPdXNz==
	msg = raw_input('tapez un message a decoder\n')
	print("Message original : " + base64.decodestring(msg))
else:
	print("Erreur lors de la saisie")

