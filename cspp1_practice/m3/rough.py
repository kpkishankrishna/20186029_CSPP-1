a= "!@#$%^&*()"
b=[]
a= a.split(" ")

for i in a:
    for j in i:
        b.append(j)
print(b)
