"""
백만 이하로 시작하는 우박수(hailstone sequence) 중 가장 긴 과정을 거치는 것은?
"""
from py_modules.timer import logging_time


def cal_hailstone_sequence(num):
    cnt = 1
    while num > 1:
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        cnt += 1
    return cnt


@logging_time
def who_has_max_seq(num):
    hailstone = 0
    max_seq = 0
    for i in range(num // 2, num+1):
        seq = cal_hailstone_sequence(i)
        if seq > max_seq:
            max_seq = seq
            hailstone = i
    print(hailstone)
    return hailstone


if __name__ == '__main__':
    who_has_max_seq(1000000)        # 8.25 sec
