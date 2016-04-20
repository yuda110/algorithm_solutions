#1001×1001 행렬을 만들었을 때, 대각선상의 숫자를 더하면?
#1. 일단 규칙부터 찾고
#2. 차근차근 더함

def sum_one_square(first_num, nth) :
    result_sum = 0
    for i in range(1, 5) :
        next_num = first_num + 2*i*nth
        result_sum += next_num
    return result_sum, next_num

def sum_diagonal(matrix) :
    first_num = 1
    result_sum = 1
    for i in range(1, int((matrix+1)/2)) :
        one_sqaure_sum, next_num = sum_one_square(first_num, i)
        first_num = next_num
        result_sum += one_sqaure_sum
    return result_sum

print(sum_diagonal(1001))