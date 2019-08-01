"""
Lexicographic permutations
0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서 1,000,000번째는 무엇입니까?
"""
from py_modules.timer import logging_time
import itertools


@logging_time
def solution(range_to):
    num = '0123456789'
    num_list = itertools.permutations(num)
    for idx, lexi_num in enumerate(num_list, 1):
        if idx == range_to:
            return ''.join(lexi_num)


if __name__ == '__main__':
    solution(1000000)
