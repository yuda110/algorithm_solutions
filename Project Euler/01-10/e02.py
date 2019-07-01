import time


# 아래 둘은 쓰레기임
# def fibo1(seq):
#     if seq == 0:
#         return 0
#     elif seq == 1:
#         return seq
#     else:
#         return fibo2(seq-1)+fibo2(seq-2)
#
#
# def fibo2(seq):
#     a, b = 1, 1
#     for i in range(seq-1):
#         a, b = b, a+b
#     return a


def fibo3(n):
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    r = 0

    while num3 <= n:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if num3 % 2 == 0:
            r += num3
    return r


def fibo4(n):
    a, b = 0, 1
    while a <= n:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


if __name__ == '__main__':
    start = time.time()
    result1 = fibo3(4000000)
    print(result1)
    print(time.time() - start)


    start = time.time()
    result2 = sum(list(fibo4(4000000)))
    print(result2)
    print(time.time() - start)
