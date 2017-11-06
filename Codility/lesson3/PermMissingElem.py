def solution(A):
    if A:
        sorted_A = sorted(A)
        for idx, n in enumerate(sorted_A, 1):
            if idx != n:
                return idx
        return sorted_A[-1]+1
    else:
        return 1

if __name__ == '__main__':
    result = solution([2, 3])
    print(result)
