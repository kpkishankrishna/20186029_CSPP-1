'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def combine_dictionary(dict_1, dict_2):
    '''input: two dictionary and output: combine dictionary with value as list
    '''
    dictionary = {}
    for word in dict_1:
        if word in dict_2:
            if word not in dictionary:
                dictionary[word] = [dict_1[word], dict_2[word]]

    for word in dict_1:
        if word not in dictionary:
            dictionary[word] = [dict_1[word], 0]
    for word in dict_2:
        if word not in dictionary:
            dictionary[word] = [0, dict_2[word]]
    return dictionary

def calculate_similarity(dict_cal):
    '''input: combine dictionary and output: value of the dictionary num/denom
    '''
    numerator = sum([key[0] * key[1] for key in dict_cal.values()])
    dict_1 = math.sqrt(sum([key[0]**2 for key in dict_cal.values()]))
    dict_2 = math.sqrt(sum([key[1]**2 for key in dict_cal.values()]))
    return numerator/(dict_1*dict_2)

def create_dic(words_l):
    '''return dictionary and input as wordlist
    '''
    dict_n = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_l:
        word = word.strip()
        if word not in stopwords and word != '':
            if word not in dict_n:
                dict_n[word] = 1
            else:
                dict_n[word] += 1
    return dict_n


def clean_string(inp_1):
    '''take string and return list
    '''
    words = inp_1.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words

def similarity(string1, string2):
    '''
        Compute the document distance as given in the PDF
    '''
    words_list1 = create_dic(clean_string(string1))
    words_list2 = create_dic(clean_string(string2))
    dict_similarity = combine_dictionary(words_list1, words_list2)
    return calculate_similarity(dict_similarity)


def load_stopwords(file_na):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_na, 'r') as file_1:
        for line in file_1:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
