a = {'lorem': 2, 'ipsum': 2, 'porem': 2}
c=[]
for i in a:
    if a[i] == 2:
        i = i+("- ##")
        c.append(i)
    else:
        i = i+("- #")
        c.append(i)
c.sort()
for i in c:
    print(i)