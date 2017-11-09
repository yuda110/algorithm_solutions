# N개의 상수로 이루어진, 비어있지 않은 리스트 A가 있다.
# A 순열(permutation)은 1부터 N 까지의 중복되지 않는 숫자의 연속이다.

def solution(A):
    sorted_a = sorted(set(A))
    if len(sorted_a) == len(A) and sorted_a[-1] == len(A):
        return 1
    else:
        return 0

if __name__ == '__main__':
    result = solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8])
    print(result)

# time complexity
    # : O(N) or O(N * log(N))