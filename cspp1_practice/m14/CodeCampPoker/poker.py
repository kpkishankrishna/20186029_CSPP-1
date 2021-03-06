'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
dict_face = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def face_values(hand):
    face_values = []
    for i in hand:
        face_values.append(dict_face[i[0]])
    face_values.sort()
    return face_values
def suit_values(hand):
    suit_values = []
    #suit_values = [s for f,s in hand]
    for i in hand:
        suit_values.append(i[1])
    return suit_values
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    '''list_1 = []
    lis_suit = []
    for i in hand:
        list_1.append(dict_face[i[0]])

    list_1.sort()
    print(list_1)
    for i in range(0, len(list_1)-1):
        if list_1[i+1] - list_1[i] != 1:
            return False
    return True
    '''
    if all([True if c in '2345A' else False for c,s in hand]):
        return True
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    return len(card_values) == 5 and (max(card_values) - min(card_values) == 4)

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    '''
    count = 0
    flag = ord(hand[0])
    for i in range(1, len(hand)):
        if flag == ord(hand[i]):
            count += 1
    if count == len(hand):
        return 3
    else:
        return 2
    '''
    return len(set([s for f,s in hand])) == 1

def five_of_kind(hand):
    pass



def four_of_kind(hand):
    #while len(set(face_values(hand))) == 2:
    a= face_values(hand)
    a.sort()
    b=[]
    c=[]
    for i in a:
        if a[0] == i:
            b.append(i)
        else:
            c.append(i)
    if len(b) == 4 and len(c) == 1:
        return True
    elif len(b) == 1 and len(c) == 4:
        return True
    else:
        return False 

     

def three_of_kind(hand):
    return len(set(face_values(hand))) == 3



def two_of_kind(hand):
    return len(set(face_values(hand))) == 4

def full_house(hand):
    a= face_values(hand)
    a.sort()
    b=[]
    c=[]
    for i in a:
        if a[0] == i:
            b.append(i)
        else:
            c.append(i)
    if len(b) == 2 and len(c) == 3:
        return True
    elif len(b) == 3 and len(c) == 2:
        return True
    else:
        return False


def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 6
    elif is_flush(hand):
        return 4
    elif is_straight(hand):
        return 3
    elif four_of_kind(hand):
        return 5
    elif three_of_kind(hand):
        return 2
    elif two_of_kind(hand):
        return 1
    else:
        return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    '''for i in key:
        for j in key:
            if key[j] != key[i]:
                return max(hands, key=hand_rank)
            else:
                return max
    '''            
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
