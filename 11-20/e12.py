#python3
import time

#def cal_triangle_num(seq) :
#    triangle_num = int((seq*(seq+1))/2)
#    return triangle_num

#def cal_factors(triangle_num) :
#    arr = [1, triangle_num]
#    for i in range(1, triangle_num+1) :
#        if triangle_num % 2 != 0 :
#            return 0
#        elif triangle_num % i == 0 :
#            count += 1
#    return count

def cal_triangle_num(seq) :
    num = 0
    arr = [num]
    for i in range(1, seq) :
        num += i
        arr.append(num)
    return arr

#def cal_factors(triangle_num) :
#    arr = [1, triangle_num]
#    for i in range(2, triangle_num) :
#        if i in arr :
#            return arr
#        if triangle_num % 2 != 0 :  #120 >> 85 seconds!
#            break
#        elif triangle_num % i == 0 :
#            arr.append(i)
#            arr.append(triangle_num/i)
#    return arr

def cal_factors(triangle_num) :
    factors = set([1, triangle_num])
    for i in range(2, triangle_num) :
        if i in factors :
            return factors
        if triangle_num % 2 != 0 : 
            break
        elif triangle_num % i == 0 :
            factors.add(i)
            factors.add(triangle_num/i)
    return factors

start_time = time.time()
for triangle_num in cal_triangle_num(1000000) :
    if len(cal_factors(triangle_num)) > 500 :
        print(triangle_num)
        break
print("--- %s seconds ---" % (time.time() - start_time))