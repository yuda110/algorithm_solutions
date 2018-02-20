def solution(A, B, K):
    result = 0
    if A >= K:
        result = B // K - (A-1) // K
    elif B >= K:
        result = B // K
    if A == 0:
        result += 1
    return result

