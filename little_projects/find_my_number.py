# The goal is to create a program where the computer chooses a random number between 1 and 100, and the user has to guess it. 
# With each attempt, the program tells the user whether their number is “too big” or “too small,” until they find the correct answer.
#
#

import random

theNumber = random.randint(1, 100)

def startingblock(rep, theNumber):
	check = num_verificator(rep)
	result = compraison(check, theNumber)

# check if it's a number between 1 and 100. 
def num_verificator(rep):
	try:
		rep = int(rep)	
	except ValueError as e:
		rep = input("Must be a number and between 1 and 100! \nRetry : ")
		return num_verificator(rep)
	if rep < 1 or rep > 100 : 
		rep = input("Must be a number and between 1 and 100! \nRetry : ")
		return num_verificator(rep)
	else : 
		return rep
	

def compraison(check, theNumber):
	if check == theNumber: 
		print("Yeah !!!! you found it ! ")
		return
	if check < theNumber:
		newrep = input("nope, try bigger : ")
	elif check > theNumber:
		newrep = input("nope, try smaller : ")
	startingblock(newrep, theNumber)

rep = input("guess which number the computer has selected. It's between 1 and 100 : ")
startingblock(rep, theNumber)


