'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels
 contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
authur@ : kpkishankrishna
'''
def main():
    '''
     the input string is in s
     remove pass and start your code here
    '''
    input_s = input()
    num_vowels = 0
    for i in input_s:
        if i in "aeiou":
            num_vowels += 1
    print(num_vowels)
if __name__ == "__main__":
    main()
