#Declaration de listes
ma_liste = [1,'deux','trois',4.5,'six']
ma_liste2 = [6,'sept',ma_liste,8]
ma_listchaine = ["liste1","test","vxson","list"]

nouvelle_liste = ma_liste + ['milieu'] + ma_liste2 #Concatenation d'une liste

#Afficher la liste
print("afficher liste")
print(nouvelle_liste)
print("\n")

#Fonctions
print("Chercher si 3 est dans la liste")
print("trois" in nouvelle_liste) #in permet de savoir si l'element est dans la liste
print("\n")

#Ordonner la liste
print(ma_listchaine.sort(reverse=True)) #Ne fonctionne pas 'none'


#ajouter un element a une liste
nouvelle_liste.append("Nouvel element")
print("ma nouvelle liste")
print(nouvelle_liste)
print("\n")


#Faire une liste qui contient des nombres de 0 a 50 sans boucle
listeNombre = list(range(5,15,2)) #range de 5 a 15 avec un pas de 2
print("list range")
print(listeNombre)
print("\n")

#print("range")
#print range(5,25,2) #fonctionne pas pour le moment
#print("\n")
