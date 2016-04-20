def sum_square(range_from, range_to) :
    sum_square = 0
    for i in range(range_from, range_to) :
        sum_square += i**2
    return sum_square

def square_sum(range_from, range_to) :
    sum = 0
    for i in range(range_from, range_to) :
        sum += i
    return sum**2

print(square_sum(1, 101) - sum_square(1, 101))