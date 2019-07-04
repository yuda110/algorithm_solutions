"""
최소공배수 LCM(Lease Common Multiple)

1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""

import functools
import operator

from py_modules.prime import prime_list
from py_decorators.timer import logging_time


def get_prime_set(num):
    prime_set = set()
    for i in range(2, num):
        primes = prime_list(i)
        prime_set.update(primes) if primes else prime_set.add(i)
    return prime_set


@logging_time
def get_lcm():
    prime_set = get_prime_set(20)
    step = functools.reduce(operator.mul, prime_set)    # 소수들을 곱한 수
    result = step
    while True:
        for i in range(1, 21):
            if result % i != 0:
                break
            elif i == 20:
                return result
        result += step


if __name__ == '__main__':
    print(get_lcm())


# def is_devidable(num_todo, num_to_devide):
#     return num_todo % num_to_devide == 0
#
#
# def is_devidable_at_range(num_todo,range_from, range_to ):
#     result = True
#     for i in range(range_from, range_to):
#         if not is_devidable(num_todo, i):
#             result = False
#             break
#     return result


# def find_devidable_min_value(range_from, range_to) :
#     num_todo = range_to
#     while True :
#         if num_todo % range_to == 0 :
#             if not is_devidable_at_range(num_todo, range_from, range_to) :
#                 pass
#                 # print(num_todo)
#             else :
#                 break
#         num_todo += range_to
#     return num_todo
#
#
# print(find_devidable_min_value(1, 20))