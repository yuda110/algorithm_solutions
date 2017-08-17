import time

def get_prime_set(num):
    prime_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime_set.add(i)
            num //= i
        if num == 1:
            break
    if num > 1:
        prime_set.add(num)
    return prime_set

def get_continuous_num():
    cnt = 0
    i = 1
    p_set2 = get_prime_set(i + 1)
    p_set3 = get_prime_set(i + 2)
    while cnt < 3:
        p_set1 = p_set2
        p_set2 = p_set3
        p_set3 = get_prime_set(i+3)
        if len(p_set1) == 3 and len(p_set2) == 3 and len(p_set3) == 3:
            if p_set1 != p_set2 and p_set2 != p_set3 and p_set3 != p_set1:
                print(i)
                print(p_set1, p_set2, p_set3)
                return i
        i += 1


if __name__ == '__main__':
    start = time.time()
    get_continuous_num()
    print(time.time() - start)