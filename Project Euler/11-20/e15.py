"""
20×20 격자의 좌상단에서 우하단으로 가는 경로의 수
중학교 수학 문제
"""
from py_modules.timer import logging_time


@logging_time
def cal_number_of_case():
    pre_case = [1]*21
    next_case = [1]*21
    for i in range(1, 21):
        for j in range(1, 21):
            next_case[j] = next_case[j-1] + pre_case[j]
            pre_case = next_case
    return next_case[-1]


if __name__ == '__main__':
    print(cal_number_of_case())
