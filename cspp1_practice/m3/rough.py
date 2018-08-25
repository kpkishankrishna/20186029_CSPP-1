a = {'This': 1, 'is': 1, 'assignment': 1, '3': 1, 'in': 1, 'Week': 1, '4': 1, 'Exam': 1}
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