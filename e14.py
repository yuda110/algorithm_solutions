import time

def cal_hailstone_sequence(num) :
    seq = 0
    while num > 1 :
        if num % 2 == 0 :
            num = num / 2
        else :
            num = 3*num + 1
        seq += 1
    return seq+1

def who_has_max_seq(range_to) :
    i = 1
    hailstone = 0
    max_seq = 0
    while i < range_to :
        if cal_hailstone_sequence(i) > max_seq :
            max_seq = cal_hailstone_sequence(i)
            hailstone = i
        i += 2
    return hailstone

start_time = time.time()
#print(who_has_max_seq(1000000))    #24seconds
print("--- %s seconds ---" % (time.time() - start_time)) 