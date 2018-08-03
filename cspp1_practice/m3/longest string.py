str = input()
max = ""
len_1 = len(str)
for i in range (len_1):
	sub = ""
	t = str[j]
	for i in range(j, len_1):
		if t <= str[i]:
		t = str[i]
		sub += t
		else:
			break
	