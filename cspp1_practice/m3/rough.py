a = [3, 2, 3, 2, 3]
a.sort()
b=[]
c=[]
for i in a:
    if a[0] == i:
        b.append(i)
    else:
        c.append(i)
print(b,c)
if len(b) == 2 and len(c) == 3:
    print(True)
elif len(b) == 3 and len(c) == 2:
    print(True)
else:
    print(False)