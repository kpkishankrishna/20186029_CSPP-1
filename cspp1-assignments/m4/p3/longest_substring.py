'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
 occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on
 to a different part of the course.
If you have time, come back to this problem after you've had a break and c
leared your head.
'''

def main():
    '''
    # the input string is in s
    # remove pass and start your code here
    '''
    str_input = input()
    str_max = ""
    len_1 = len(str_input)
    for j in range(len_1):
        sub_str = ""
        t_1 = str_input[j]
        for i in range(j, len(str_input)):
            if t_1 <= str_input[i]:
                t_1 = str_input[i]
                sub_str += t_1
            else:
                break
        if len(str_max) < len(sub_str):
            str_max = sub_str
    print(str_max)
if __name__== "__main__":
    main()
