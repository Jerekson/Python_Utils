



try:
	s = "abd"
	it = iter(s)
	print(it)
	print(next(it))
	print(next(it))
	print(next(it))
	print(next(it))	
except StopIteration as e:
	print("youhou StopIteration for the last one")
	print(e)