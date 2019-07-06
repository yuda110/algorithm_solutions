"""
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
이 때 10,001번째의 소수를 구하세요.
"""

from py_modules.prime import is_prime
from py_modules.timer import logging_time


#def is_prime_num(num) :    #16.15 seconds
#    i = 3
#    while  i < num :
#        if num % i != 0 :
#            i += 2
#        else :
#            return False
#    return True


# def is_prime_num(num):   # 0.21 seconds
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True


@logging_time
def find_prime_num(seq_range_to):
    num = 3
    prime_seq = 1
    prime_num = 0
    while prime_seq < seq_range_to:
        if is_prime(num):
            prime_seq += 1
            prime_num = num
        num += 2
    return prime_num


if __name__ == '__main__':
    print(find_prime_num(10001))
