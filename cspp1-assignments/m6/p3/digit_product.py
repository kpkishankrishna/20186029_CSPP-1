'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    int_a = abs(int_input)
        int_n = 0
    int_pro = 1
    while int_a > 0:
        int_n = int_a%10
        int_pro = int_pro*int_n
        int_a = int_a//10
        print(int_pro)

if __name__ == "__main__":
    main()
