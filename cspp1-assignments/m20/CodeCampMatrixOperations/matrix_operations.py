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
    pass

def main():
    # read matrix 1
    m= int(input('rows'))
    n = int(input('columns'))
    mat1 =[]
    for i in range(m):
        mat.append([])
    for i in range(m):
        for j in range(n):
            mat[i].append(j)
            mat[i][j]=0
    for i in range(m):
        for j in range(n):
            print("enter the rows",i+1,"enter the coulmns", j+1)
            mat[i][j] = int(input())

    # read matrix 2
    m= int(input('rows'))
    n = int(input('columns'))
    mat2 =[]
    for i in range(m):
        mat.append([])
    for i in range(m):
        for j in range(n):
            mat[i].append(j)
            mat[i][j]=0
    for i in range(m):
        for j in range(n):
            print("enter the rows",i+1,"enter the coulmns", j+1)
            mat[i][j] = int(input())
    print(mat1,mat2)

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    
print(mat)

if __name__ == '__main__':
    main()