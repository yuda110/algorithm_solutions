"""
이백만(2,000,000) 이하 소수의 합은 얼마입니까?
"""

from py_modules.timer import logging_time
from py_modules.prime import is_prime


# 5.4sec
@logging_time
def sum_prime_nums(num):
    result = 2 + 3 + 5 + 7
    cnt = 0
    for n in range(3, num+1, 2):
        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:  # sieve of Eratosthenes
            cnt += 1
            pass
        elif is_prime(n):
            result += n
    return result


if __name__ == '__main__':
    sum_prime_nums(2000000)
