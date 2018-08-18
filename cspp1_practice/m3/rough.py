docs = "my name is my name is krishna prasad krishna prasad"
import re
words = docs.lower().strip().replace('\'', '')
regex = re.compile('[^a-z]')
words = regex.sub(" ", words).split(" ")
print(words)


big_dict = {}
for i in words:
    if i not in big_dict:
        big_dict[i] = 1
    else:
        big_dict[i] += 1
print(big_dict)
