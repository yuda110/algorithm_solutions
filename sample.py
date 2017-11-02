import re
import math
import primesieve
import time


# 소인수분해
# def get_prime (num):
#     factor_list = []
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             factor_list.append(i)
#             num = num / i   # WOW!!!
#         if num == 1:
#             break
#     return factor_list
def get_prime (num):    # very slow...
    factor_list = []
    if num % 2 == 0: factor_list.append(2)

    for i in range(3, num, 2):
        if num % i == 0:
            factor_list.append(i)
            num = num / i   # WOW!!!
        if num == 1:
            break
    return factor_list

def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i     # num = num / i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


# 약수의 개수
def counting_divisor(num):
    cnt = 1

    for i in range(2, int(num**0.5) + 1):
        each_divisor_cnt = 0
        if num % i == 0:
            while num % i == 0:
                each_divisor_cnt += 1
                num = num / i
                cnt *= (each_divisor_cnt+1)
        if num == 1:
            return cnt
    return cnt


def get_gcd(m, n):  # Euclidean algorithm
    while n != 0:
        t = m % n
        (m, n) = (n, t)
        # print(m, n)
    return abs(m)


def get_lcm(m, n):  # Least common multiple
    gcd = get_gcd(m, n)
    lcm = gcd * (m/gcd) * (n/gcd)
    return int(lcm)


def factorial(num):
    if num < 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result


def get_divisor(num):
    divisor_list = []
    for i in range(2, num):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list


def counting_rational_num(numerator, range_to):
    divisor_list = get_divisor(numerator)
    cnt = 0

    for n in range(1, range_to+1):
        remainder_list = [n%f for f in divisor_list]
        if 0 not in remainder_list:
            cnt += 1
    return cnt*2

# radius(반지름), diameter(지름)
pi = 3

def foo(radius, total_seq, seq):
    total_area = (radius**2)*pi
    each_len = radius/total_seq
    each_area = 0
    for i in range(1, seq+1):
        inner_radius = radius-(each_len*i)
        inner_area = (inner_radius**2)*pi
        each_area = total_area - inner_area
        total_area = inner_area
    return each_area


def get_divisor_list(num, i, d_list):
    if num % i == 0:
        d_list.append(i)
        num = num / i
        if num < i:
            return d_list
        else:
            get_divisor_list(num, i, d_list)
    else:
        get_divisor_list(num, i+1, d_list)

# def is_infinite_prime(deno, nume):  # 분모, 분자


if __name__ == '__main__':
    # num = 3391500
    start = time.time()

    print(get_lcm(168, 2*3**2*5**2*11))