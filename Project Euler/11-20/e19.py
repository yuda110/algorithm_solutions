"""
20세기 (1901년 1월 1일 ~ 2000년 12월 31일) 에서, 매월 1일이 일요일인 경우는 총 몇 번?
"""
from py_modules.timer import logging_time
import datetime


@logging_time
def solution():
    result = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            d = datetime.date(y, m, 1)
            if d.weekday() == 6:
                result += 1
    return result


if __name__ == '__main__':
    solution()
