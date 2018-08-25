'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string,no_of_lines):
    
    one_list = []
    for i in range(no_of_lines):
        for j in range(string[i]):
            one_list.append(string[i][j])
    return one_list


#     c={}
# for i in a:
#     if i not in c:
#         c[i]=1
#     else:
#         c[i]+=1

    

            
def main():
	no_of_lines = int(input())
	string = []
	for i in range(no_of_lines):
		string.append(input().strip().split(" "))
	

	print(tokenize(string,no_of_lines))

    

if __name__ == '__main__':
    main()
