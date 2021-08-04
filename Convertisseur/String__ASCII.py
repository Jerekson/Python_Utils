# Décoder un code ascii qui est en héxa : 
# en utilisant Python : 
str = "4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465"
str.decode("hex")




def decode():
    toDecode = input('tapez un message a decoder\n')


def encode():
    toDecode = input('tapez un message a decoder\n')
    print("ui", toDecode)


choix = input("Encode ou Decode ? \n")

if choix == "encode" or choix == "Encode":
	encode()
elif choix == "decode" or choix == "Decode":
    decode()
else:
	print("Erreur lors de la saisie")