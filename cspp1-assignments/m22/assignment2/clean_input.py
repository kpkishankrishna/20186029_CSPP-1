'''
author@: kpkisankrishna
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    string = string.split(" ")
    new_list=[]
    clean_list = []
    clean_str=""
    for i in string:
        for j in i:
            new_list.append(j)
    for i in new_list:
        if i in "1234567890qwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFSAXCVBNM":
            clean_list.append(i)
    for i in clean_list:
        clean_str += i
    return clean_str


def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
