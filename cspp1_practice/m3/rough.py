if __name__ == '__main__':
    main()
    # N = int(raw_input())
def main ():
    list = []
    lines = int(input())
    for i in range(lines) :
        thislist = input().split(" ")
        if (thislist[0] == "insert"):
            list[thislist[1]] = thislist[2]
        elif (thislist[0] == "remove"):
            list.remove(thislist[1])
        elif (thislist[0] == "append") :
            list.append(thislist[1])
        elif (thislist[0] == "print"):
            print(list)
        elif (thislist[0] == "reverse"):
            list.reverse()
        elif (thislist[0] == "pop"):
            list.pop(len(list))
        elif (thislist[0] == "sort"):
            list.sort