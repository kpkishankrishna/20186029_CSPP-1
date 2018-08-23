def mult_matrix(m_1, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    add_m = re_mat(len(m_1), len(m_2[0]))
    if len(m_1[0]) == len(m_2):
        for i in range(len(m_1)):
            for j in range(len(m_2[0])):
                for k in range(len(m_2)):
                    add_m[i][j] += m_1[i][k] * m_2[k][j]
        return add_m
    print("Error: Matrix shapes invalid for mult")
    return None
            
def re_mat(rows, columns):
    '''
    gives empty rows and columns
    '''
    multi_matrix = [[0 for i in range(columns)] for j in range(rows)]
    return multi_matrix
                 

def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    add_m = re_mat(len(m_1), len(m_2[0]))
    if len(m_1) == len(m_2) and len(m_1[0]) == len(m_2[0]):
        for i in range(len(m_1)):
            for j in range(len(m_1[0])):
                add_m[i][j] = m_1[i][j] + m_2[i][j]
        return add_m  
    else:
        print("Error: Matrix shapes invalid for addition")
        return None  
    

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat = []
    list_input = input().split(",")
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_mat_row = input().split()
        if columns == len(list_mat_row):
            mat.append([int(i) for i in list_mat_row])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return mat
    



def main():
    # read matrix 1
    '''
    main function
    '''
    matrix_1 = read_matrix()
    if matrix_1 is None:
        exit()
    matrix_2 = read_matrix()
    if matrix_2 is None:
        exit()
    print(add_matrix(matrix_1,matrix_2))
    print(mult_matrix(matrix_1, matrix_2))


if __name__ == '__main__':
    main()
