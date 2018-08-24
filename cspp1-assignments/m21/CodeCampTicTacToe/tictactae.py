'''

author@: kpkishankrishna
'''
def winner_check(matrix):
    '''
it gives the output coditions
    '''
    # return_string = ''
    # if matrix[0][0] == matrix[1][1] == matrix[2][2]:
    #     return_string = matrix[0][0]
    # elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
    #     return_string = matrix[0][2]
    # elif matrix[0][0] == matrix[1][0] == matrix[2][0]:
    #     return_string = matrix[0][0]
    # elif matrix[0][1] == matrix[1][1] == matrix[2][1]:
    #     return_string = matrix[0][1]
    # elif matrix[0][2] == matrix[1][2] == matrix[2][2]:
    #     return_string = matrix[0][2]
    # elif matrix[0][0] == matrix[0][1] == matrix[0][2]:
    #     return_string = matrix[0][0]
    # elif matrix[1][0] == matrix[1][1] == matrix[1][2]:
    #     return_string = matrix[1][0]
    # elif matrix[2][0] == matrix[2][1] == matrix[2][2]:
    #     return_string = matrix[2][0]
    # else:
    #     return_string = "invalid input"
    # return return_string
    flip_matrix = zip(*matrix)
    if is_verification_rows_columns(flip_matrix, check_variable) or\
        is_verification_rows_columns(matrix, check_variable):
        return True
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == check_variable) or\
        (matrix[0][2] == matrix[1][1] == matrix[2][0] == check_variable):
        return True
    else:
        return False
def vaild_check(matrix):
    '''
   It checks for the condition
    '''
    tic1_list = full_string(matrix)
    if tic1_list.count('x') > 5 or  tic1_list.count('o') > 5  or\
      tic1_list.count('x') == tic1_list.count('o'):
        return "invalid game"
    for _ in range(len(tic1_list)):
        for j in tic1_list:
            if j not in 'ox.':
                return "invalid input"
    if (tic1_list.count('x') == 4 and tic1_list.count('o') == 5) or\
     (tic1_list.count('x') == 5 and tic1_list.count('o') == 4):
        return "draw"

    return 1
def empty_tictac():
    '''
    # it converts the input into lists
    '''
    matrix = []
    for _ in range(3):
        list_temp = input().split()
        matrix.append(list_temp)
    return matrix
def full_string(matrix):
    '''
    it converts thr lists of list into string
    '''
    list_temp = []
    for i in matrix:
        list_temp.extend(i)
    return list_temp
def main():
    '''
    it is the main function
    '''
    inp_tic = empty_tictac()
    clean_string = full_string(inp_tic)
    output = vaild_check(clean_string)
    if output == 1:
        print(winner_check(inp_tic))
    else:
        print(output)


if __name__ == '__main__':
    main()
