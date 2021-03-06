'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''



# helper function to load the stop words from a file
import re
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    # words = text.lower().strip().replace('\'', '')
    # regex = re.compile('[^a-z]')
    # words = regex.sub(" ", words).split(" ")
    # return words
    words = re.sub('[^a-z]'," ", text.lower().replace('\'', "").strip()).split()
    stopwords = load_stopwords("stopwords.txt")
    words = [word.strip() for word in words if word not in stopwords and len(word) >0]
    return words
# def create_dic(words):
#     '''return dictionary and input as wordlist
#     '''
#     dict_n = {}
#     stopwords = load_stopwords("stopwords.txt")
#     for word in words_l:
#         word = word.strip()
#         if word not in stopwords and word != '':
#             if word not in dict_n:
#                 dict_n[word] = 1
#             else:
#                 dict_n[word] += 1
#     return dict_n

def build_search_index(documents):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    search_index = {}
    # iterate through all the docs
    for document_id, document in enumerate(documents):
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
        words_document_list = word_list(document)
        # clean up doc and tokenize to words list
        for word in words_document_list:
            if word not in search_index:
                search_index[word] = []
                search_index[word].append((document_id, words_document_list.count(word)))
            else:
                if (document_id, words_document_list.count(word)) not in search_index[word]:
                    search_index[word].append((document_id, words_document_list.count(word)))
    return search_index

        # add or update the words of the doc to the search index

    # return search index
    # dictionary = {}
    # stop_word = load_stopwords("stopwords.txt")
    # for index, line in enumerate(docs):
    #     if index not in stop_word and index != '':
    #         list_of_words = remove_stopwords(word_list(line), stop_word)
    #         for word in set(list_of_words):
    #             if word in dictionary:
    #                 dictionary[word].append((index, list_of_words.count(word)))
    #             else:
    #                 dictionary[word] = [(index, list_of_words.count(word))]
    # return dictionary
    
    




# helper function to print the search index
# use this to verify how the search index looks
# def remove_stopwords(word, stop_word):
#     list_1 = word
#     for w_1 in word:
#         if w_1 in stop_word:
#             list_1.remove(w_1)
#     return list_1
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
