# N개의 상수로 이루어진 리스트 A가 있다.
# 이때 A 안에 '없는' 가장 '작은' 자연수(0보다 큰)를 리턴한다.

def solution(A):
    if max(A) < 1:
        return 1
    else:
        sorted_a = sorted(set([a for a in A if a > 0]))
        for idx, val in enumerate(sorted_a, 1):
            if idx != val:
                return idx
        return sorted_a[-1]+1


if __name__ == '__main__':
    result = solution([-1, -3, 1, 3, 4, 5])
    print(result)