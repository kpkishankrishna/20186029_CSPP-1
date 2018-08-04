n = "abcd"
len_1 = len(n)
r = ""
q = ""
for i in range(0,len_1):
	if i%2 == 0:
		r = r + n[i]
	else:
		q = q + n[i]
print(r)
print(q)