#python3
import time
import itertools

def cal_lexicographic_permutation(range_to) :
    seq = 1
    num = '0123456789'
    num_list = itertools.permutations(num)
    for lexi_num in num_list :
        if seq == range_to :
            return "".join(lexi_num)
        seq += 1

start_time = time.time()
print(cal_lexicographic_permutation(1000000))
print("--- %s seconds ---" % (time.time() - start_time))