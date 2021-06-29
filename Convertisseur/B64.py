#!/usr/bin/env python
import base64
#PYTHON 2 ONLY

choix = input("Encode ou Decode ? \n")

if choix == "encode" or choix == "Encode":
	pass
elif choix == "decode" or choix == "Decode":
	# texte : QmlsbHlPdXNz==
	msg = input('tapez un message a decoder\n')
	print("Message original : " + str(base64.urlsafe_b64decode(msg),)) # base64.decodestring(msg)
else:
	print("Erreur lors de la saisie")

