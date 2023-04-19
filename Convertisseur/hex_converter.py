#python3

import binascii

def string_to_hex():
    toDecode = input('\nexpected anything like that : 0x7061756 or 74657374 or 0x74/x65/x73/x74 \ntapez un message a decoder\n')
    decoded = ""
    if toDecode[:2] == "0x":
        decoded = bytes.fromhex(toDecode[2:]).decode("utf-8")
    else:
        decoded = bytes.fromhex(toDecode).decode('utf-8')
    print(decoded)

def hex_to_string():
    toEncode = input('\nutf-8 string is expected \ntapez un message a encoder\n')
    encoded = toEncode.encode('utf-8').hex()
    print("0x"+encoded)

choix = input("Encode String vers Hex (1) \n \
Decode Hex vers String (2) \n")
if choix == "1":
	hex_to_string()
elif choix == "2":
    string_to_hex()
else:
	print("Erreur lors de la saisie")
