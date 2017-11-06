# 비어있지 않은 리스트 A 에는 N 개의 숫자가 있다.
# 상수 P 는 0 < P < N 의 조건을 가진다.
# 리스트 A 를 둘로 나누면 A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# 가장 작은 두 파트의 차이값(절댓값)을 구하시오.

def solution(A):
    left_sum = A[0]
    right_sum = sum(A[1:])
    min_diff = abs(left_sum - right_sum)
    for i in range(1, len(A)-1):
        left_sum += A[i]
        right_sum -= A[i]
        if abs(left_sum - right_sum) < min_diff:
            min_diff = abs(left_sum - right_sum)
    return min_diff

    # for p in range(1, len(A)):
    #     diff = abs(sum(A[:p]) - sum(A[p:]))
    #     if min_diff:
    #         if min_diff > diff:
    #             min_diff = diff
    #     else:
    #         min_diff = diff
    # return min_diff

if __name__ == '__main__':
    result = solution([3, 1, 2, 4, 3])
    print(result)
