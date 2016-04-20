import math

def sum_factorial(num) :
    facto = math.factorial(num)
    facto_arr = list(str(facto))
    facto_sum = sum(int(i) for i in facto_arr)

    return facto_sum

print(sum_factorial(100))