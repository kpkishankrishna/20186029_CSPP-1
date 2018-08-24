def read_input():
    input_1=[]
    for i in range(3):
        input_1.append(input().split(" "))
    return(input_1)
    
def one_list(game_input):
    one_list = []
    for i in range(len(game_input)):
        for j in range(len(game_input[i])):
            one_list.append(game_input[i][j])
    return one_list

def valid_game_check(one_list_1):
    for i in one_list_1:
        if i not in 'xo.':
            return 1
        elif one_list_1.count('x') > 5 or one_list_1.count('o') > 5:
            return False
        elif one_list_1.count('x') - one_list_1.count('o') > 1 or one_list_1.count('o') - one_list_1.count('x') >1:
            return False
        else:
            return True

def check_horizontal(game_input):
    for i in game_input:
        if i.count(x)==3:
            return "x"
        if i.count(o)==3:
            return "o"
        else:
            return None
def check_vertical(one_list_1):
    for i in one_list_1(3):
        if i == i+3 == i+6:
            if i == "x":
                return "x"
            elif i == "o":
                return "o"
            else:
                return None
def check_diagonal(one_list_1):
    for i in one_list_[1]:
        if i == i+4 == i+8:
            if i == "x":
                return "x"
            elif i == "o":
                return "o"
            else:
                return None
    for i in one_list_1[2:3]:
        if i == i+2 == i+4:
            if i == "x":
                return "x"
            elif i == "o":
                return "o"
            else:
                return None



def check_winner(game_input, one_list_1):
    #print(game_input)
    # for i in game_input:
    #     if set(game_input[i]) == x:
    #         return x
    #     elif set(game_input[i]) == o:
    #         return o
    # for i in one_list_1:
    #     if one_list_1[i] == one_list_1[i+3] == one_list_1[i+6]:
    if check_horizontal(game_input) != None:
        return check_horizontal(game_input)
    elif check_vertical(one_list_1) != None:
        return check_vertical(game_input)
    elif check_diagonal(one_list_1) != None:
        return check_diagonal(game_input)
    else:
        return("draw")
def main():
    game_input = read_input()
    one_list_1 = one_list(game_input)
    if valid_game_check(one_list_1) == 1:
        print("invalid input")
    elif valid_game_check(one_list_1) == False:
        print("invalid game")
    elif valid_game_check(one_list_1):
        print(check_winner(game_input,one_list_1))
if __name__ == '__main__':
    main()