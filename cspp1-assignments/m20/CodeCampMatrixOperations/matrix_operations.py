def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    # for i in range(row_size):
    #     matrix_1.append(list(map(int,input().rstrip().split(" "))))
    # matrix_ = []
    # row_size=int(matrix_[0])
    # col_size=int(matrix_[1])
    # print(matrix_1)
    matrix_1 = []
    list_input = input().split(",")
    rows,columns = int(list_input[0],list_input[1])
    for i in range(rows):
        matrix = input().split(" ")
        if length(matrix) == rows:
            matrix_1.append([int(value) for value in matrix])
        print("error")
    print(matrix_1)




def main():
    # read matrix 1


    # m= int(input('rows'))
    # n = int(input('columns'))
    # mat1 =[]
    # for i in range(m):
    #     mat.append([])
    # for i in range(m):
    #     for j in range(n):
    #         mat1[i].append(j)
    #         mat1[i][j]=0
    # for i in range(m):
    #     for j in range(n):
    #         print("enter the rows",i+1,"enter the coulmns", j+1)
    #         mat1[i][j] = int(input())

    # read matrix 2


    # m= int(input('rows'))
    # n = int(input('columns'))
    # mat2 =[]
    # for i in range(m):
    #     mat2.append([])
    # for i in range(m):
    #     for j in range(n):
    #         mat2[i].append(j)
    #         mat2[i][j]=0
    # for i in range(m):
    #     for j in range(n):
    #         print("enter the rows",i+1,"enter the coulmns", j+1)
    #         mat2[i][j] = int(input())
    # print(mat1,mat2)

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    


if __name__ == '__main__':
    main()
