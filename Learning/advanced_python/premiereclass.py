class Informatique(object):
	def __init__(self, langage): #C'est le constructeur, tous les elements qu'on passe en parametre de la class, on les lies aux attribut de la classe
		#self : c'est ce qu'on a en parametre de la classe
		#self == this en groovy
		self.langage = langage
	def les_langages(self):
		for line in self.langage:
			print(line)

langage_script = Informatique(["Le bash","Le Perl","Le Python"]) #On fait notre variable et on appel la classe en y passant un dict en para
#puis met tout le contenu dans self.langage

autre_langages = Informatique(["Langage C","Le java"]) #Pareil

langage_script.les_langages() #On appel la fonction dans la classe
autre_langages.les_langages()

