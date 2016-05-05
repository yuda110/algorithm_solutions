#python3
import math

def cal_digit(x, y) :
    num = pow(x, y)
    digit_sum = 0
    for i in list(str(num)) :
        digit_sum += int(i)
    return digit_sum

print(cal_digit(2, 1000))