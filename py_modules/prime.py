# Prime module


# 단, n은 2 이상인 수
def is_prime(n):
    if n == 2:
        return True
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def prime_list(target):
    result = []
    for i in range(2, target):
        if target % i == 0:
            result.append(i)
            target = target / i
        if target == 1:
            break
    return result
