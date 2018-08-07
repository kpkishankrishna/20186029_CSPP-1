'''
Author@: kpkishankrishna
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns
 the sum of digits of given number.
# This function takes in one number and returns one number.
'''
def sumofdigits(n_1):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_1 == 0:
        return 0
    return n_1%10 + sumofdigits((n_1//10))


def main():
    '''
    main function
    '''
    a_1 = input()
    print(sumofdigits(int(a_1)))

if __name__ == "__main__":
    main()
