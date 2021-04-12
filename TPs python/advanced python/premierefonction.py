def bonjour(): #Declaration d'une fonction
	var = 1 
	while var < 8: #Tant que var n'est pas a 8, on affiche "bonjour" ainsi que le numero de var
		print("bonjour n°",var)
		var = var + 1

print("Fonction sans parametre")
bonjour() #Appel de la fonction bonjour


#Ecrire le prennom dans l'input et dans la fonction on retourne le prenom a l'envers

def newName(monNom): #Cette fois il y'a des paramètres entre les parenthèses
	return monNom[::-1]

monNom = input("\nFonction avec parametre\nentrez votre prenom ")
print(newName(monNom)) #Affichage + Appel de la fonction newName avec monNom en tant que parametre
