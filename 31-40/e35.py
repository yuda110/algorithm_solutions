import primesieve
from itertools import permutations
from collections import deque
import time

def is_prime(num):
    result = False
    for i in range(2, num):
        if num > 2 and num % i == 0 :
            return False
        else :
            result = True
    return result

def is_circular_prime(prime):
    result = False
    prime_str_list = list(str(prime))
    prime_deque = deque(prime_str_list)
    for i in range(len(prime_deque)):
        prime_deque.rotate()
        rotated_num = int(''.join(prime_deque))
        if is_prime(rotated_num) == True :
            result = True
        else :
            result = False
            break
    return result

def get_circular_prime(range_to):
    count = 1    #2!
    prime_list = primesieve.generate_primes(range_to)      #[2, 3, 5, 7, 11, 13, 17, 19....]
    for prime in prime_list:
        if is_circular_prime(prime) == True :
            count += 1
    return count

start_time = time.time()
print(get_circular_prime(100000))
print("--- %s seconds ---" % (time.time() - start_time))