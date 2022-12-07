#Variables
texte = "Hello world!"

fichier = open('fichier1.txt','r') #Mode de lecture

#Fermeture du fichier
fichier.close()

#Reouverture du fichier
fichier = open('fichier2.txt','w') #Mode d'ecriture
fichier.write(texte)
fichier.close()
