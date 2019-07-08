"""
세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
"""

from py_modules.timer import logging_time

# 0.03sec
@logging_time
def find_pita():
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            c = 1000 - a - b
            if a*a + b*b == c*c and a < b < c:
                return a*b*c


if __name__ == '__main__':
    find_pita()
