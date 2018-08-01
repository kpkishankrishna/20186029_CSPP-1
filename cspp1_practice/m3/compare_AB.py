'''
@author :kpkishankrishna
compare the given variables a and b
'''
varA = 4
varB = 6
if (type(varA) == str) or (type(varB) == str):
    print("string involved")
elif varA > varB :
    print("bigger")
elif varA==varB :
    print("equal")
else:
    print("smaller")

