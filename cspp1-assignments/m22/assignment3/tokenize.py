'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    
    # one_list = []
    # for i in range(len(string)):
    #     for j in range(string[i]):
    #         one_list.append(string[i][j])
    # print(one_list)


    c={}
    for i in a:
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
    return c

    

            
def main():
	no_of_lines = int(input())
	string = []
	for i in range(no_of_lines):
		string.append(input().strip().split(" "))
	

	print(tokenize(string))

    

if __name__ == '__main__':
    main()
