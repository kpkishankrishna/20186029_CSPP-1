input_1 = "My name is Krishna Prasad 1234"
input_2 = "My name is gangadhar singh"
import re

# dict_3 = {}
# for i in dict_1:
#     if i not in dict_3:
#         dict_3[i] = 1
#     else:
#         dict_3[i] += 1
# print(dict_3)
def clean_string(words):
    words_1 = input_1.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words_1 = regex.sub(" ", words_1).split(" ")
    print(words_1)
def create_dic(words_l):
    '''return dictionary and input as wordlist
    '''
    dict_n = {}
    for word in words_l:
        word = word.strip()
        if word != '':
            if word not in dict_n:
                dict_n[word] = 1
            else:
                dict_n[word] += 1
    return dict_n
def combine_dictionary(dict_one, dict_two):
    '''input: two dictionary and output: combine dictionary with value as list
    '''
    dict_combine = {}
    for word in dict_one:
        if word in dict_two:
            if word not in dict_combine:
                dict_combine[word] = [dict_one[word], dict_two[word]]

    for word in dict_one:
        if word not in dict_combine:
            dict_combine[word] = [dict_one[word], 0]
    for word in dict_two:
        if word not in dict_combine:
            dict_combine[word] = [0, dict_two[word]]
    return dict_combine

a = create_dic(clean_string(input_1))
b = create_dic(clean_string(input_2))
print(combine_dictionary(a,b))