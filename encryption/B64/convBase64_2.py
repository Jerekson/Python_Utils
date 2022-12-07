import base64
from binascii import Error


def encode():
    msg = input("Entrez un message a encoder : ")
    print(f"Message encodé : {base64.encodebytes(bytes(msg, 'utf-8')).decode('utf-8')}")


def decode():
    msg = input("Entrez un message a decoder : ")
    try: #Verifier qu'il s'agit bien d'une Base 64 dans le decode
        print(f"Message décode : {base64.decodebytes(bytes(msg, 'utf-8')).decode('utf-8')}")
    except Error:
        raise Exception("Le message entre n'est pas en base64")

encode()
decode()
