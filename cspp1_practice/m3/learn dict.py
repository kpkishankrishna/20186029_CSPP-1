import string
s = string.ascii_lowercase[:]
print(s)
d = {}
for i in s:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1
print(d)
print("...................")
d_1 = {}
for i in d:
	if d[i] not in d_1:
		d_1[d[i]] = []
		d_1[d[i]].append(i)
	else:
		d_1[d[i]].append(i)

print(d_1)