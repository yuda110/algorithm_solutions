
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_lychrel_num(n, cnt=1):
    n += int(str(n)[::-1])

    if is_palindrome(n):
        return False
    elif cnt >= 50:
        return True
    else:
        return is_lychrel_num(n, cnt+1)


if __name__ == '__main__':
    import time
    start = time.time()
    cnt = 0
    for n in range(1, 10001):
        if is_lychrel_num(n):
            cnt += 1
    print(cnt)
    print(time.time()-start)
