#python3
import time

#def is_prime_num(num) :
#    i = 3
#    while  i < num :
#        if num % i != 0 :
#            i += 2
#        else :
#            return False
#    return True
def is_prime_num(num) :
    for i in range(2, int(num**0.5) + 1):
        if num % i==0:
            return False
    return True

def sum_prime_nums(range_to) :
    prime_sum = 2+3+5+7
    for num in range(7, range_to+1) :
        if num % 2 !=0 and num % 3 !=0 and num % 5 !=0 and num % 7 !=0 :    #sieve of Eratosthenes
            if is_prime_num(num) :
                prime_sum = prime_sum + num
        num += 2
    return prime_sum

start_time = time.time()
print(sum_prime_nums(2000000))
print("--- %s seconds ---" % (time.time() - start_time))