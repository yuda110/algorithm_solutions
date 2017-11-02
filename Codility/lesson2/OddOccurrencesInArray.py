
def solution(A):
    A = sorted(A)
    for i in range(0, len(A), 2):
        try:
            if A[i] == A[i+1]:
                pass
            else:
                return A[i]
        except: return A[i]
