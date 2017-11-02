def solution(A, K):
    if A:
        if len(A) <= K:
            while len(A) < K:
                K -= len(A)
        to_be_moved_list = A[-K:]
        del A[-K:]
        return to_be_moved_list + A
    else:
        return A

if __name__ == '__main__':
    print(solution([1, 2], 5))