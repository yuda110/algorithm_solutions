# 개구리는 강의 한 열에 있다.(position 0)

def solution(X, A):
    leaf_set = set()
    for idx, val in enumerate(A):
        leaf_set.add(val)
        if len(leaf_set) == X:
            return idx
    return -1

# def solution(X, A):
#     target = A.index(X)
#     for i in range(target, len(A)):
#         if len(set(A[:i+1])) == X:
#             return i
#     return -1


if __name__ == '__main__':
    result = solution(3, [1, 3, 1, 3, 2, 1, 3])
    print(result)
