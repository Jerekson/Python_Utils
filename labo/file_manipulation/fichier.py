#Variables
texte = "Hello world!"

#fichier = open('fichier1.txt','r') #Mode de lecture

#Fermeture du fichier
#fichier.close()

#Reouverture du fichier
fichier = open('testlog.log','w') #Mode d'ecriture
fichier.write(texte)
fichier.close()
