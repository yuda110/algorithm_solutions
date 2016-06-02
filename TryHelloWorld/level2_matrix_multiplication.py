def cal_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    return row, col

def productMatrix(A, B):
    row_a, col_a = cal_matrix(A)
    row_b, col_b = cal_matrix(B)
    #answer = [[0]*col_b]*row_a
    answer = [[0]*col_b for x in range(row_a)]
    
    for i in range(row_a):
        for j in range(col_b):
            result = 0
            for k in range(row_b):
                result += A[i][k] * B[k][j]
            answer[i][j] = result
            
    return answer