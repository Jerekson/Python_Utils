class Vehicule(object):
	def voir(self):
		print("Nous sommes dans voir() de la classe Vehicucle")

class Voiture(Vehicule):
	def voir(self): #polymorphisme ; utilise la fonction de la classe parent
		print("Nous sommes dans voir() de la classe voiture")

class Bateau(Vehicule):
	def voir(self):
		print("Nous sommes dans voir() de la classe bateau")

class Avion(Vehicule):
	def voir(self):
		print("Nous sommes dans voir() de la classe avion")

#Instanciation des classes
v1 = Voiture()
b1 = Bateau()
a1 = Avion()

list_vehicule = [v1, b1, a1]
for vehicule in list_vehicule:
	vehicule.voir()
