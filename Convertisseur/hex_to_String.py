import binascii

# this decode is only on python3
def decode():
    toDecode = input('\nexpected anything like that : 0x7061756 or 74657374 or 0x74/x65/x73/x74 \ntapez un message a decoder\n')
    decoded = bytes.fromhex(toDecode).decode('utf-8')
    print(decoded)

# this decode is only on python3
def encode():
    toEncode = input('\nutf-8 string is expected \ntapez un message a decoder\n')
    encoded = toEncode.encode('utf-8').hex()
    print(encoded)

choix = input("Encode ou Decode ? \n")
if choix == "encode" or choix == "Encode":
	encode()
elif choix == "decode" or choix == "Decode":
    decode()
else:
	print("Erreur lors de la saisie")