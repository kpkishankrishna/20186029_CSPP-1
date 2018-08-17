'''
    Document Distance - A detailed description is given in the PDF
'''
import string
import re
import math
def clean_text(text_input):
    words = text_input.lower().strip()
    regex = re.compile('[^a-z]')
    words = regex.sub("", words).split(" ")
    return words
def create_dict(words_list):
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords and words_list.len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary
def combine_dictionary(dict1, dict2):
    dictionary = {}
    for word in dictionary_one, dictionary_two:
        if word in dictionary_two:
            dictionary[word] = [dictionary_one[word], dictionary_two[word]]

    for word in dictionary_one:
        if word not in dictionary:
            dictionary[word] = [dictionary_one[word], 0]
    for word in dictionary_two:
        if word not in dictionary:
            dictionary[word] = [0, dictionary_two[word]]
    return dictionary

def calculate_similarity(dict_values):
    numerator = sum([k[0] * k[1] for k in dictionary_values()])
    d1_a = math.sqrt(sum([k[0] ** 2 for k in dictionary_values()]))
    d2_a = math.sqrt(sum([k[1] ** 2 for k in dictionary_values()]))
    return numerator/(d1_a*d2_a)




def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary_one = clean_text(dict1)
    dictionary_two = clean_text(dict2)
    dictionary = combine_dictionary(dictionary_one, dictionary_two)
    return calculate_similarity(dictionary)
    



def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
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
