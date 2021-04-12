import string
# Chiffrement de cesar

print("Chiffrement de cesar\n")
letters = string.ascii_lowercase #On recupere ce que contien ascii lowercase (lettre alphabetique minuscule

key = input("nombre pour le decalage : ") #On choisit le decalage
key = int(key)

trans_table = letters[key:] + letters[0:key] 
trans = string.maketrans(letters, trans_table)

text = raw_input("texte a chiffrer :\n") #On recupere le text a chiffrer
text = str(text)

print(text.translate(trans)) #On affiche le texte chiffre
