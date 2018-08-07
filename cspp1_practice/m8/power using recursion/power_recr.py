# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recur_power(a, b):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if b == 1:
        return a
    elif b == 0:
        return (1)
    else:
        return a*(recur_power(a,b-1))

def main():
    data = input()
    data = data.split()
    print(recur_power(float(data[0]),int(data[1])))   

if __name__== "__main__":
    main()