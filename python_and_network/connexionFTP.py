import socket

host = "ftp.ibiblio.org"
port = 21

def fini(): #verifie si le socket recois quelque chose ?
	data = s.recv(1024)
	print(data)
	if data == "":
		pass

#Connexion au serveur ftp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
fini()

# on met l'utilisateur et le mot de passe (en binaire)
# La fonction send permet d'envoyer des commandes
s.send(b"USER anonymous\r\n")
fini()

s.send(b"PASS toto@tata.fr\r\n")
fini()

s.send(b"QUIT\r\n")


s.close
