#Declaration des tuples
tuple = (1, 'un', 2, 'deux', 3.14) #un tuple commence a l'index 0
tuple2 = (12, 'douze', tuple, 'onze') #Ce tuple contient le precedent tuple a l'index 2

#test print
print("Tout le tuple2")
print(tuple2,"\n") #Afficher tout le tuple 2

print("index 2 du tuple2")
print(tuple2[2],"\n") #Afficher l index 2 du tuple2

print("premier element du tuple")
print(tuple[0],"\n") #Afficher le premier element du tuple

print("la chaine Itescia est dans tuple ?")
print('itescia' in tuple,"\n") #Verifie si 'itescia' est dans le tuple

print("Combien de fois il ya 'deux' dans tuple2")
print(tuple2.count('deux'),"\n") #Compte le nombre de fois qu'il y a deux dans tuple2 (ne rentre pas dans les autres tuple)

print("longueur du tuple")
print(len(tuple),"\n") #Affiche a longueur du tuple
