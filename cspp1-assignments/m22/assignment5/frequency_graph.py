'''
author@: kpkishankrishna
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	'''
    '''

    # dictionary into list

    list_dict = []
    for i in dictionary:
        if dictionary[i] == 2:
            i = i+(" - ##")
            list_dict.append(i)
        else:
            i = i+(" - #")
            list_dict.append(i)
    list_dict.sort()
    return list_dict

def main():
    '''
    main function
    '''
    dictionary = eval(input())
    list_dict = frequency_graph(dictionary)
    for i in list_dict:
        print(i)

if __name__ == '__main__':
    main()
