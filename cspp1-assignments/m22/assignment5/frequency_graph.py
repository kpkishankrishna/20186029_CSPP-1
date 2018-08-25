'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    c=[]
    for i in dictionary:
        if dictionary[i] == 2:
            i = i+("- ##")
            c.append(i)
        else:
            i = i+("- #")
            c.append(i)
    c.sort()
    return c

def main():
    dictionary = eval(input())
    list_dict = frequency_graph(dictionary)
    for i in list_dict:
        print(i)

if __name__ == '__main__':
    main()
