import time
import primesieve

def get_prime1(num):
    prime_list = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime_list.append(i)
            num //= i
        if num == 1:
            break

    if num > 1:
        prime_list.append(num)
    return prime_list


def get_prime2(num):
    prime_list = []
    if num % 2 == 0:
        prime_list.append(2)
    for i in range(3, num, 2):
        if num % i == 0:
            prime_list.append(i)
            num //= i
    return prime_list


def get_divisor(num):
    i = 2
    divisor_list = []
    while i * i <= num:
        if num % i != 0:
            i += 1
        else:
            num //= i
            divisor_list.append(i)
    if num > 1:
        divisor_list.append(num)
    return divisor_list


# 정수가 아닌 유리수
def counting_rational_num(nume, range_to):
    cnt = 0
    prime_list = get_prime1(nume)
    for i in range(1, range_to+1):
        if 0 in [i % p for p in prime_list]:
            pass
        else:
            cnt += 1
    return cnt


def get_factor(num):
    factor_dict = {}
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i in factor_dict:
                factor_dict[i] += 1
            else:
                factor_dict[i] = 1
            num //= i
        else:
            i += 1

    if num > 1:
        if num in factor_dict:
            factor_dict[num] += 1
        else:
            factor_dict[num] = 1

    return factor_dict


if __name__ == '__main__':
    num = 230  # 135475990
    start = time.time()

    get_factor(168)

    # cnt = counting_rational_num(14, 300)
    # print(cnt)
    # print(get_prime1(num))
    # print(time.time() - start)

    # start = time.time()
    # divisor_list = get_divisor(num)
    # print(divisor_list)
    # print(time.time() - start)
    #
    # start = time.time()
    # prime_list = get_prime3(num)
    # print(prime_list)
    # print(time.time() - start)
