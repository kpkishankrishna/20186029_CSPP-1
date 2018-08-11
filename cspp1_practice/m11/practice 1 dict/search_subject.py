d = {}
def create_dict(List):
    for i in range(0,len(List), 2):
        if List[i] not in d:
            d[List[i]] = List[i+1].split(',')
    return d

def search_subject(str_subject):
    l = []
    for i in d:
        if str_subject in d[i]:
            l.append(i)
    return l
  
def main():
    n = int(input())
    L = []
    for i in range(n):
        list_input = input().split(" ")
        L.extend(list_input)
    return create_dict(L)


d = main()
print(search_subject("c3"))