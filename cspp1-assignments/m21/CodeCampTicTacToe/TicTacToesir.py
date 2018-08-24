
def main():
    intac = tictac_input()
    valid_check = check_valid(intac)
    if valid_check == True:
        if valid_game(intac)
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
    pass



if __name__ == '__main__':
    main()
