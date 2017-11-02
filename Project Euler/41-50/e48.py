import time

sum = 0
for i in range(1, 1001):
    sum += i**i
print(sum % (10**10))

def get_last_nums(range_to, digit):
    sum = 0
    for i in range(1, range_to+1):
        sum += i**i
    last_ten_nums = sum % (10**digit)
    return last_ten_nums


if __name__ == '__main__':
    start = time.time()
    # get_last_nums(1000, 10)
    # last_ten_nums = get_last_nums(1000, 10)
    # print(last_ten_nums)
    #
    # print(time.time() - start)
