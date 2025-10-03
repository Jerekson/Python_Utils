class Classdeux:
	test_alive = "ui"
	
	def __init__(self, vartest, testinf):
		self.vartest = vartest
		self.testinf = "AAAAAAH"
		self.i = 12345
		self.test_alive = "Hello World from " + __name__

	def alive(self):
		return("Hellow World! def from " + __name__)

class Subclassdeux(Classdeux):

	def __init__(self, ui):
		self.ui = ui



if __name__ == "__main__":
	myclass = Classdeux("ui", "no")
	mysubclass = Subclassdeux("xe")

	print(myclass.test_alive)
	print(mysubclass.test_alive)
	print(mysubclass.alive())
