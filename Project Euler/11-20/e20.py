"""
100! 의 자리수를 모두 더하면 얼마입니까?
"""
from py_modules.timer import logging_time
import math


@logging_time
def solution1(num):
    facto = math.factorial(num)
    facto_arr = list(str(facto))
    facto_sum = sum(int(i) for i in facto_arr)
    return facto_sum


@logging_time
def solution2(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    result = sum([int(i) for i in str(f)])
    return result


if __name__ == '__main__':
    solution1(100)
    solution2(100)
