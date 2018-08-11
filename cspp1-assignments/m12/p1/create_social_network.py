'''
    Assignment-1 Create Social Network
'''

def create_social_network(list_1):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    dictionary_sn = {}
    for i in range(0, len(list_1), 3):
        if list_1[i+1] in 'follows':
            d[list_1[i]] = list_1[i+2].split(',')
        else:
            dictionary_sn = {}

    return dictionary_sn

def main():
    '''
        handling testcase input and printing output
    '''
    list_1 = []
    lines = int(input())
    for i in range(lines):
        inp_l = input().split(" ")
        list_1.extend(inp_l)


    print(create_social_network(list_1))

if __name__ == "__main__":
    main()
