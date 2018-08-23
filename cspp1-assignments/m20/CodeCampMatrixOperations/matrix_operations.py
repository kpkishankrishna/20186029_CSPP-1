def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(m1)
    columns = len(m2[0])
    mult_matrix = [[0]*columns]*rows



def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    matrix_1 = []
    rows = len(m1)
    columns = len(m1[0])
    add_matrix = [[0]*columns]*rows
    print(add_matrix)
    for i in range(rows):
        for j in range(columns):
            add_matrix[i][j] = m1[i][j]+m2[i][j]
            print("i",str(i),"j",str(j),add_matrix[i][j])
    return add_matrix

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix_1 = []
    list_input = input().split(",")
    rows,columns = int(list_input[0]),int(list_input[1])
    for i in range(rows):
        matrix = input().split(" ")
        if len(matrix) == rows:
            matrix_1.append([int(i) for i in matrix])
    return matrix_1




def main():
    # read matrix 1
    matrix_1 = read_matrix()
    matrix_2 = read_matrix()
    matrix_3 = add_matrix(matrix_1,matrix_2)
    print(matrix_3)


if __name__ == '__main__':
    main()
