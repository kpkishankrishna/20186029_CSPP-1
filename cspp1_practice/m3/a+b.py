num = 6
r = ''
while num > 0:
	r = r + str(num%2)
	num = num//2
print(r)