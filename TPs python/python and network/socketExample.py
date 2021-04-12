import socket #bibliotheque socket

print("creation du socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation de l'objet socket   sockStream (connexion tcp)     afinet (toujours present lors de la connexion
print("socket FAIT")
s.connect(('lesgeniesduweb',22)) #Connexion + concantenation de l'ip et du port
print("connexion au site fait")
data = s.recv(2048) #Recuperation des donnees
print(data)
s.close #fermer le socket
