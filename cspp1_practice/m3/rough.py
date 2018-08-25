a = "lorem ipsum porem lorem ipsum porem"
a=a.split(" ")
c={}
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1
print(c)