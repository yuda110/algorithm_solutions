#1 ~ 9 pandigital
import time
import re
from itertools import permutations

def get_permutation_list():
    permu_list = permutations('123456789', 9)
    return permu_list

def get_pandigital_formula(permutation_list):
    result_set = set()
    for permu in permutation_list:
        first_num = int(permu[0])
        second_num = int(permu[1]+permu[2]+permu[3]+permu[4])
        third_num = int(permu[5]+permu[6]+permu[7]+permu[8])
        if first_num*second_num == third_num:
            result_set.add(third_num)
        first_num = int(permu[0]+permu[1])
        second_num = int(permu[2]+permu[3]+permu[4])
        if first_num*second_num == third_num:
            result_set.add(third_num)
    return sum(result_set)

start = time.time()
print(get_pandigital_formula(get_permutation_list()))
print(time.time() - start)