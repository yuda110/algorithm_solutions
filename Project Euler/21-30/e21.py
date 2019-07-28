"""
서로 다른 두 정수 a, b에 대하여 d(a) = b 이고 d(b) = a 이면
a, b는 친화쌍이라 하고 a와 b를 각각 친화수(우애수)라고 합니다.
10000 이하의 친화수들을 모두 찾아서 그 합을 구하세요.
"""
from py_modules.timer import logging_time


def d(num):
    factors = {1}
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            factors.add(i)
            factors.add(num//i)
    return sum(factors)


@logging_time
def solution(range_to):
    result = 0
    for a in range(2, range_to):
        b = d(a)
        if a == d(b) and a != b:
            result += a
    return result


if __name__ == '__main__':
    solution(10000)
