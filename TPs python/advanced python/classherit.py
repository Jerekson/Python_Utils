class Pere: #class parent
	def ou_suis_je(self):
		print("Dans la classe Pere") 

class Herite(Pere): #class qui herite de la class parent
	pass #Permet de laisser la class vide sans creer d'erreur

#Appel de la foncion de la class parent via la class Herite
Herite().ou_suis_je()
