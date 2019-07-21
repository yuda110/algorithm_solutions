def solution(x, y):
    return sum([int(i) for i in str(x**y)])


if __name__ == '__main__':
    solution(2, 1000)
