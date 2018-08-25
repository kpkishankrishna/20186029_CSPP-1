'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    string = string.strip().split(" ")
    return (string)
    

            
def main():
	no_of_lines = int(input())
	string = ""
	for i in range(no_of_lines):
		string += input()
	print(tokenize(string))

    

if __name__ == '__main__':
    main()
