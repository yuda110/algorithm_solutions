import time

def get_irrational_num_list(range_to):
    irrational_num = ''
    num = 1
    while len(irrational_num) < range_to :
        irrational_num += str(num)
        num += 1
    return irrational_num

def get_nth_num(range_to):
    irrational_num = get_irrational_num_list(range_to)
    nth = 1
    result = 1
    while nth <= range_to:
        result = result * int(irrational_num[nth-1])
        nth = nth * 10
    return result

start = time.time()
print(get_nth_num(1000000))
print(time.time() - start)