def main():
    l= []
    n = int(input()).split(" ")
    for i in range(n):
        l_in = int(input())>split(" ")
        l.extend(l_in)
    print(create_function(l,n))
def create_dictionary(l,n):
    dict_1 = {}
    for i in range(0, len(l) , 2):
        if i not in dict_1:
            dict_1[int(l[i])] = int(l[i+1])
        else:
            dict_1[int(l[i])] += int(l[i+1])
    return dict_1





