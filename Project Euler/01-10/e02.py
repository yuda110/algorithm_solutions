import time


def fibo1(seq):
    if seq == 0:
        return 0
    elif seq == 1:
        return seq
    else:
        return fibo2(seq-1)+fibo2(seq-2)


def fibo2(seq):
    a, b = 1, 1
    for i in range(seq-1):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    start = time.time()
    # result = fibo2(33)
    # result = fibo1(438)
    result = fibo2(10)
    print(result)
    # print(time.time() - start)
