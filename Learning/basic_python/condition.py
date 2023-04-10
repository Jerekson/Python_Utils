#Declaration des variables
choix = input("choisir un mot a ecrire parmis ceux la : monTest | ui | bonjour : ")

#Conditions if
print("\n\nCONDITION IF\n")
if choix == "monTest": #Si le choix est 'monTest'
	print("cela fonctionne") #dire que cela fonctionne
elif choix == "ui": #sinon si le choix est 'ui'
	print("ok")
elif choix == "bonjour":
	print("Excellent choix")
else:			#Sinon dire que ce n'est pas bon (pour cet exemple)
	print("Il faut respecter la consigne l'ami")


#Conditions while
print("\n\nCONDITION WHILE\n")
var = input("entrez une phrase : ")
i=0
while i < len(var): #Tant que i est inferieur a la longueur de la phrase
	print(var[i]) #Afficher chaque caractere de la dite phrase
	i=i+1 #incrementation de i


#Conditions for
print("\n\nCONDITION FOR\n")
listfor = ["list1","list2","list3","list","test","ui","bl"]
for cpt in listfor: #pour cpt dans ma list, j'affiche le contenu de la liste a la position cpt
	print(cpt)

print("\n")

#La meme avec un tuple
tuple = ("tuple","test","ui")
for cpt in tuple: #pour cpt dans mon tuple, j'affiche le contenu de mon tuple a la position cpt
	print(cpt)

print('\n')

#boucle for plus complexe
for a in range(1,11):
	for b in range(1,11):
		for c in range(1,11): #trois boucle for imbrique
			nb1 = a*100+b*10+c
			nb2 = a**3+b**3+c**3

			if nb1==nb2:
				print(str(nb1) + " " + str(a) + " " + str(b) + " " + str(c))
