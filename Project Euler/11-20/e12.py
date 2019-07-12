"""
1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 합니다.
500개 이상의 약수를 갖는 가장 작은 삼각수는 얼마입니까?
(소인수분해 한 뒤 각각의 지수에 1을 더하여 곱하면 약수의 개수가 나온다.)

- 정답은 당연히 짝수일 것이니 짝수인 삼각수만 약수를 구함
- 약수의 개수를 구할 때 해당 수의 제곱근까지만 돌림
"""

from py_modules.timer import logging_time


def cal_factors(num):
    factors = len({1, num})
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            factors += 2
    return factors


@logging_time
def solution(target):
    step = 1
    num = 0
    factors = 0
    while target > factors:
        num += step
        step += 1
        if num % 2 == 0:
            factors = cal_factors(num)
    print(num, factors)
    return factors


if __name__ == '__main__':
    solution(500)
