"""
그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?
"""

if __name__ == '__main__':
    square_sum = sum([i**2 for i in range(1, 101)])
    sum_square = sum(range(1, 101))**2
    diff = abs(square_sum - sum_square)
    print(diff)
