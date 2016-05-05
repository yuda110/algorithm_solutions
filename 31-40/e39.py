import time, cProfile
import math

def get_right_triangle_cnt(p):
    right_triangle_list = set()
    for a in range(1, round(p/2)):
        for b in range(1, round(p/2)):
            c = p - (a + b)
            if 	a*a + b*b == c*c : 
                right_triangle_list.add(c)
    return len(right_triangle_list)

def get_max_right_triangle_cnt(range_from, range_to, step):
    max_cnt = 0
    max_p = 0
    for p in range(range_from, range_to, step) :
        each_cnt = get_right_triangle_cnt(p)
        if each_cnt > max_cnt :
            max_cnt = each_cnt
            max_p = p
    return max_p

start = time.time()
print(get_max_right_triangle_cnt(4, 1001, 2))
print(time.time()-start)