#Exercise : Biggest Exercise
#Write a procedure, called biggest,
# which returns the key corresponding to the entry with
# the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxl = 0
    ans = 0
    for i in  aDict:
        if type(aDict[i]) == list or type(aDict[i]) == tuple:
            if maxl < len(aDict[i]):
                maxl = len(aDict[i])
                ans = i
        if maxl == 0 and ans == 0:
            maxl = 1
            ans = 1
    return(ans, maxl)


def main():
    # aDict={}
    # s=input()
    # l=s.split()
    # if l[0][0] not in aDict:
    #     aDict[l[0][0]]=[l[1]]
    # else:
    #     aDict[l[0][0]].append(l[1])
    aDict = {1: [1, 2, 3], 2: (1, 3, 4, 5), 3:1, 4:2, 5:10.53627829}    
    print(biggest(aDict))


if __name__== "__main__":
    main()