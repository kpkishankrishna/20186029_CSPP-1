one_list_1 = ["x","o","."]
for i in one_list_1:
        if i not in 'xo.':
            print(1)
if one_list_1.count('x') > 5 or one_list_1.count('o') > 5:
    print(False)
elif one_list_1.count('x') - one_list_1.count('o') > 1 or one_list_1.count('o') - one_list_1.count('x') >1:
    print(False)
else:
    print(True)