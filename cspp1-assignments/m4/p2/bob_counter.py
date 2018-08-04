'''
author@ : kpkishankrishna
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

def main():
    
    '''
    the input string is in s
    remove pass and start your code here
    '''
    input_s = input()
    num_bob = 0
    value_bob = "bob"
    for i in range(len(input_s)-2):
        if input_s[i] + input_s[i+1] + input_s[i+2] == value_bob:
            num_bob += 1
    print(num_bob)
if __name__ == "__main__":
    main()
