
def main():
    intac = tictac_input()
    valid_check = check_valid(intac)
    if valid_check:
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
    for i in intac:
        if i not in "xo.":
            return 1
        elif intac.count('x') > 5 or intac.count('o') > 5:
            return False
        elif intac.count('x') - intac.count('o') > 1 or intac.count('o') - intac.count('x') >1:
            return False
        else:
            return True



if __name__ == '__main__':
    main()
