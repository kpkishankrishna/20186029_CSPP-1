def sum1(a,b):
	if b == 1:
		return a
	else:
		return a + sum1(a,b-1)
print(sum1(4,3))