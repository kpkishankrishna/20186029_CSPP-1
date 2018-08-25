'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    string = string.split(" ")
    new_list=[]
    for i in string:
    	for j in i:
    		new_list.append(j)
    print(new_list)

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
