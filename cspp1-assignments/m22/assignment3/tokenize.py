'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    creating a dictionary with frequency
    '''
    
    dictionary_final = {}
    for element_in_dic in string:
        if element_in_dic not in dictionary_final:
            dictionary_final[element_in_dic] = 1
        else:
            dictionary_final[element_in_dic] += a1
    return dictionary_final

def main():
    '''
    main function
    '''
    no_of_lines = int(input())
    # string = []
    # string.append(input().split(" "))
    # for i in string:
    #     string = i
    # print(string)
    string = []
    for i in range(no_of_lines):
      string.extend(input().strip().split(" "))
    print(tokenize(string))



if __name__ == '__main__':
    main()
