

def is_triangle(n):
    return int(n*(n + 1) / 2)


def calc_pentagonal(n):
    return int(n*(3*n - 1) / 2)


def calc_hexagonal(n):
    return int(n*(2*n - 1))



if __name__ == '__main__':
    p = 165
    h = 143
    h = 84*p + 97*h - 38
    print(h*(2*h - 1))
