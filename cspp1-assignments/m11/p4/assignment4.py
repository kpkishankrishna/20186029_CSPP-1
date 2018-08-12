#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this
    # function
    sum_1 = 0
    for i in hand:
        sum_1 += hand[i]
    return sum_1

def main():
    n_1 = input()
    adict_1 = {}
    for i in range(int(n_1)):
        del i
        data = input()
        l_1 = data.split()
        adict_1[l_1[0]] = int(l_1[1])
    print(calculate_handlen(adict_1))
        


if __name__ == "__main__":
    main()
