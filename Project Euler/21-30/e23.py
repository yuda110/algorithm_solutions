"""
자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 초과수라고 합니다.
두 초과수의 합으로 나타낼 수 없는 모든 양의 정수의 합은?
"""
from py_modules.timer import logging_time


def get_measure_sum(num):
    result = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            result.add(i)
            result.add(num//i)
    return sum(result)


@logging_time
def solution(limit):
    sum_abundant = set()
    abundant_list = [n for n in range(12, limit) if get_measure_sum(n) > n]
    for i in abundant_list:
        for j in abundant_list:
            if i+j < limit:
                sum_abundant.add(i+j)
    result = sum(range(1, limit)) - sum(sum_abundant)
    return result


if __name__ == '__main__':
    solution(28123)
