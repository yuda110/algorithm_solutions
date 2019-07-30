"""
먼저 모든 이름을 알파벳 순으로 정렬합니다.
각 이름에 대해서, 그 이름을 이루는 알파벳에 해당하는 숫자(A=1, B=2, ..., Z=26)를 모두 더합니다.
여기에 이 이름의 순번을 곱합니다.

names.txt에 들어있는 모든 이름의 점수를 계산해서 더하면 얼마입니까?
"""
from py_modules.timer import logging_time


def get_name_list():
    f = open('names.txt', 'r')
    names = f.read()
    name_list = names.replace('"', "").split(',')
    name_list.sort()
    return name_list


@logging_time
def solution():
    a_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
    name_list = get_name_list()
    result = 0
    for idx, name in enumerate(name_list, 1):
        score = sum([a_list.index(a)+1 for a in name])
        score *= idx
        result += score
    return result


if __name__ == '__main__':
    solution()
