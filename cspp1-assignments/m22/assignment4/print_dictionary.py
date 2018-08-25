'''
author@: kpkishankrishna
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    dictionary into list
    '''
    list_dict = []
    for i in dictionary:
        if dictionary[i] == 2:
            i = i+(" - 2")
            list_dict.append(i)
        else:
            i = i+(" - 1")
            list_dict.append(i)
    list_dict.sort()
    return list_dict


def main():
    '''
    main function
    '''
    dictionary = eval(input())
    list_dict = print_dictionary(dictionary)
    for i in list_dict:
        print(i)


if __name__ == '__main__':
    main()
