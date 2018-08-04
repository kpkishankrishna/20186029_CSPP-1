'''
author@ : kpkishankrishna
printing swapped characters and changing special characters.
'''
n = "abcd"
r = ""
q = ""
if len(n)%2 != 0:
    n = n + 'X'
len_1 = len(n)
for i in range(0,len_1):
    if i%2 == 0:
        r = r + n[i]
    else:
        q = q + n[i]
p = ""
for i in range(0,len(r)):
    p = p + q[i]
    p = p + r[i]
print(p)
