#python3
#각 자리 숫자를 5제곱해서 더했을 때 자기 자신이 되는 수들의 합
#1) 각자리 5제곱을 미리 계산해두고
import time
import math


square_arr = []
for i in range(0, 10) :
    square_arr.append(i ** 5)

def sum_out_squares_of_five(*args) :
    result = 0
    for a in args:
        result+=square_arr[a]
    return result
    
def is_square_of_five():
    result_sum = 0
    for a in range(1, 10) :
        for b in range(0, 10) :
            for c in range(0, 10) :
                for d in range(0, 10) :
                    four_num = 1000*a + 100*b + 10*c + d
                    if sum_out_squares_of_five(a,b,c,d) == four_num :
                        result_sum += four_num
                    for e in range(0, 10) :
                        five_num = 10000*a + 1000*b + 100*c + 10*d + e
                        if sum_out_squares_of_five(a,b,c,d,e) == five_num :
                            result_sum += five_num
                        for f in range(0, 10) :
                            six_num = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f
                            if sum_out_squares_of_five(a,b,c,d,e,f) == six_num :
                                result_sum += six_num
    return result_sum

start_time = time.time()
print(is_square_of_five())
print("--- %s seconds ---" % (time.time() - start_time))