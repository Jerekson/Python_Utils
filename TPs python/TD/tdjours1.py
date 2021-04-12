#Infos :
#Un programme qui permet a l'utilisateur d'entrer un mot puis l'utilisateur decidera de ce qu'il fera de sa chaine

#Declaration des variables


pchoix = input("""Vous souhaitez manipuler une chaine ou des nombres ? 
Entrez " chaine " ou " nombre " en fonction de votre choix
""")


#En fonction du premier choix "chaine" ou "nombre"
if pchoix == "chaine":
	maChaine = input("entrez une chaine de caractere que vous souhaitez ")

	choix = input("""\nque voulez vous en faire parmis les choix proposes (indice, ecrivez ce que vous voulez)
	ajouter un mot ou un phrase apres celle que vous avez choisi : mot
	ajouter un element pour en faire une liste : ajout
	savoir le nombre de caractere que contient le mot : combien
	\n""")


	#En fonction du choix (manipulation d'une chaine)
	if choix=="mot": #ajouter un nouveau mot
		mot = input("quel mot ou caractere souhaitez vous ajouter ? ")
		nouvMot = maChaine +" "+mot
		print(nouvMot)
	elif choix=="ajout": #Faire une liste avec le nouveau mot et le precedent mot
		mot = input("quel mot ou caractere souhaitez vous ajouter pour faire la liste ? ")
		maList = [maChaine, mot]
		print(maList)
	elif choix=="combien": #donner le nombre de caractere du mot maChaine
		print(len(maChaine))
	else:
		print("Vous ne respectez pas la consigne")
elif pchoix == "nombre":
	nombre = input("entez votre nombre ")

	choixn = input("""choisissez 
	addition
	soustraction
	multiplication
	""")

	nombre2 = input("entez le nouveau nombre ")

	nombre = int(nombre)
	nombre2 = int(nombre2)

	#En fonction du choix (manipulation des nombres)
	if choixn == "addition":
		addi = nombre+nombre2
		print(addi)
	elif choixn == "soustraction":
		sous = nombre-nombre2
		print(sous)
	elif choixn == "multiplication":
		mult = nombre*nombre2
		print(mult)
	else:
		print("respectez la condition")
else:
	print("Vous ne respectez pas la consigne")
