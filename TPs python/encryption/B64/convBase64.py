#!/usr/bin/env python
import base64
# A EXECUTER EN PYTHON 2

# texte : QmlsbHlPdXNz==
msg = input('tapez un message a decoder\n')

# Verifier que c'est bien une B64 (via expression reguliere)
# Verifier : que le contenu de la chaine ne comporte pas de caractere speciaux mais que les deux derniers caracteres sont des egales "=="


print("Message original : " + base64.decodebyte(msg))
