
def main():
    intac = tictac_input()
    valid_check = check_valid(intac)
    if valid_check(intac):
        if valid_game(intac):
            pass
        else:
            print("invalid game")    
    else:
        print("invalid input")

def tictac_input():
    intac=[]
    for i in  range(3):
        intac.append(input().strip().split())
    return intac
def check_valid(intac):
    for i in intac:
        for j in i:
            if j not in ["x","o","."]:
                return False
    else:
        return True
def valid_game(intac):
    for i in one_list_1:
        if i not in "xo.":
            return 1
        elif one_list_1.count('x') > 5 or one_list_1.count('o') > 5:
            return False
        elif one_list_1.count('x') - one_list_1.count('o') > 1 or one_list_1.count('o') - one_list_1.count('x') >1:
            return False
        else:
            return True



if __name__ == '__main__':
    main()
