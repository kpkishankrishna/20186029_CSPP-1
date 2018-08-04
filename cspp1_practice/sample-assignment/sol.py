'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and
# returns the factorial of given number.
# This function takes in one number and returns one number.
'''
def main():
    S = input()
    count = 0
    for i in S:
        if i in "aeoiu":
            count += 1
    print(count)



if __name__ == "__main__":
    main()
