#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(te):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return(te[0: len(te)+1: 2])
    

def main():
    data = input()
    data = data.split()
    te=()
    for j in range(len(data)):
        te += ((data[j]),)
    print(oddTuples(te))
        

if __name__ == "__main__":
    main()