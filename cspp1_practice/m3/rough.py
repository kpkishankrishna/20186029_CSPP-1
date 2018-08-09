letters_guessed = ['a','b', 'c']
for i in range(chr(65)):
    if i not in letters_guessed:
        str2 += i
print(str2)