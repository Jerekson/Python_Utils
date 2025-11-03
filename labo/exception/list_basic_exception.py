

def simple_int_except():
	while True:
		try:

			x = int(input("enter a number : "))
			break
		except ValueError as e:
			print(e)

def dontunderstand():
	try:
	    raise Exception('spam', 'eggs')
	except Exception as inst:
		print(type(inst))    # the exception type
		print(inst.args)     # arguments stored in .args
		print(inst)          # __str__ allows args to be printed directly,
							# but may be overridden in exception subclasses
		x, y = inst.args     # unpack args
		print('x =', x)
		print('y =', y)

if __name__ == "__main__":
	# simple_int_except()
	dontunderstand()