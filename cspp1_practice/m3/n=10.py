S = input("")
V = 0
for I in S:
    if I in ('a', 'e', 'i', 'o', 'u'):
        V += 1
print(V)
