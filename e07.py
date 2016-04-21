#python3
import time

#def is_prime_num(num) :    #16.15 seconds
#    i = 3
#    while  i < num :
#        if num % i != 0 :
#            i += 2
#        else :
#            return False
#    return True
def is_prime_num(num) :     #0.21 seconds
    for i in range(2, int(num**0.5) + 1):
        if num % i==0:
            return False
    return True

def find_prime_num(seq_range_to) :
    num = 3
    prime_seq = 1
    prime_num = 0
    while prime_seq < seq_range_to :
        if is_prime_num(num) == True :
            prime_seq += 1
            prime_num = num
        num += 2
    return prime_num

start_time = time.time()
print(find_prime_num(10001))
print("--- %s seconds ---" % (time.time() - start_time))