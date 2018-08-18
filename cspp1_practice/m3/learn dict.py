import string
file1 = "Krisha kriSha prasAd _ 1 is .a ?good guy"
file2 = "gangadhar gangadHar sIngh _ 1 iS .a ?good guy"
words = file1.lower().split(' ')
print(words)
word2 =file2.lower().split(' ')
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped)
stripped2 = [w.translate(table) for w in word2]
dict_1 = {}
dict_2 = {}
lis_1= []
cnt = 1
cnt2 = 1
for i in stripped:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1
print(dict_1)
for i in stripped2:
    if i not in dict_2:
        dict_2[i] = cnt
    else:
        dict_2[i] = cnt+1
print(dict_2)
for i in dict_1:
    if i in '1234567890':
        i += ' '
for i in dict_2:
    if i in '1234567890':
        i += ' '

print(dict_1)
print(dict_2)