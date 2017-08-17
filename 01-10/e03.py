import time


def prime_factor(target):
    last_prime = 0
    i = 2
    while target != 1:
        while target % i == 0:
            last_prime = i
            target = target / i
        if target == 1:
            break
        i += 1
    return last_prime

def prime_factor2(target):  # 위의 함수보다 0.001초 정도 빠름
    result = 0
    for i in range(2, target):
        if target % i == 0:
            result = i
            target = target / i
            print(result)
        if target == 1:
            break
    return result

def is_prime(target):
    for i in range(2, int(target**0.5)+1):
        if target % i == 0:
            return False
        if target == 1:
            break
    return True


if __name__ == '__main__':
    start = time.time()
    # prime_result = prime_factor(600851475143)
    prime_result = prime_factor2(600851475143)
    print(time.time() - start)
    #
    # print(is_prime(11))
