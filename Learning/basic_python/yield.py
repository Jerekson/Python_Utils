## About Yield functionnality 
def count_up_to(n):
	for number in range(1, n+1):
		yield number

result = count_up_to(5)
print(next(result))
print(next(result))
print(next(result))
