#python3
import time


def cal_triangle_num(seq):
    num = 0
    arr = [num]
    for i in range(1, seq):
        num += i
        arr.append(num)
    return arr


def cal_factors(triangle_num):
    factors = {1, triangle_num}
    for i in range(2, triangle_num):
        if i in factors:
            return factors
        if triangle_num % 2 != 0:
            break
        elif triangle_num % i == 0:
            factors.add(i)
            factors.add(triangle_num/i)
    return factors

start_time = time.time()
for triangle_num in cal_triangle_num(1000000):
    if len(cal_factors(triangle_num)) > 500:
        print(triangle_num)
        break
print("--- %s seconds ---" % (time.time() - start_time))
