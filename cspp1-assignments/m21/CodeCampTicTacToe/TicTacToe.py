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
    print(one_list)
def valid_game_check(one_list):
    for i in one_list:
        if i not in "xo.":
            return False
        elif one_list.count(x) > 5 or one_list.count(o) > 5:
            return False
        elif one_list.count(x) - one_list.count(o) > 1 or one_list.count(o) - one_list.count(x) >1:
            return False
        else:
            return True


def check_winner(game_input):
    pass



def main():
    game_input = read_input()
    one_list_1 = one_list(game_input)
    if valid_game_check(one_list_1) == False:
        print("invalid game")
    else:
        return check_winner(game_input)


    
    


if __name__ == '__main__':
    main()