#!/usr/bin/env python
import base64

def decode():
	msg = input('\nexpected anything like that : QmlsbHlPdXNz== or NzQ2NTczNzQ= \ntapez un message a decoder\n')
	print("Message original : " + str(base64.urlsafe_b64decode(msg),)) 

def encode():
	msg = input('\ntapez un message a decoder\n')
	print(base64.b64encode(msg.encode('ascii')))


choix = input("Encode ou Decode ? \n")

if choix == "encode" or choix == "Encode":
	encode()
elif choix == "decode" or choix == "Decode":
    decode()
else:
	print("Erreur lors de la saisie")