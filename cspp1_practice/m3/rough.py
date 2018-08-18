# import re
def load_stopwords(filename):
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(string):
    regex = re.compile('[^a-z]')
    return [regex.sub("", w.strip()) for w in string.lower().split(" ")]
def build_search_index(docs):
    dict_1 = {}
    STOP_WORD = load_stopwords("stopwords.txt")
    for index, line in enumerate(docs):
        LIST_ = remove_stopwords(word_list(line), STOP_WORD)
        for word in set(LIST_):
            if word in dict_1:
                dict_1[word].append((index, LIST_.count(word)))
            else:
                dict_1[word] = [(index, LIST_.count(word))]
    return dict_1

def remove_stopwords(word, STOP_WORD):
    LIST_1 = word
    for w_1 in word:
        if w_1 in STOP_WORD:
            LIST_1.remove(w_1)
    return LIST_1
def print_search_index(index):
keys = sorted(index.keys())
for key in keys:
    print(key, " - ", index[key])
def main():
    '''
        main function
    '''
    documents = []
    lines = int(input())
    for i in range(lines):
        documents.append(input())
        i += 1

    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()