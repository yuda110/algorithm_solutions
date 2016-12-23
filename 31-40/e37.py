import time
import primesieve

def is_prime(num):
    if primesieve.generate_n_primes(1, num)[0] == num:  
        pass
    else : 
        return False
    return True

def is_still_prime(num):
    str_num =str(num)
    for i in range(len(str_num)):
        delete_left_side_num = int(str_num[i:])
        delete_right_side_num = int(str_num[:i+1])
        if is_prime(delete_left_side_num) and is_prime(delete_right_side_num) :
            pass
        else:
            return False
    return True

def get_still_prime_sum(range_from, range_to):
    prime_list = primesieve.generate_primes(range_from, range_to)
    result_cnt = 0
    result_sum = 0
    for prime in prime_list:
        if is_still_prime(prime):
            result_sum += prime
            result_cnt += 1
            if result_cnt == 11 :
                break
    return result_sum

start_time = time.time()
print(get_still_prime_sum(10, 1000000))
print(time.time() - start_time)