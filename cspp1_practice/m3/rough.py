a= "!@#$%^&*()"
b=[]
c=""
a= a.split(" ")

for i in a:
    for j in i:
        b.append(j)
for i in b:
    c+=i
print(c)

