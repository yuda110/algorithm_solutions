import itertools
from primesieve import generate_primes

def get_biggest_decimal_pandigital(n):
    max_pan = 0
    permu_obj = itertools.permutations(range(1, n+1))
    for pan in permu_obj:
        each_pan = int(''.join(map(str,pan)))
        if len(generate_primes(each_pan, each_pan)) > 0  and each_pan > max_pan:
            max_pan = each_pan
    return max_pan

for i in range(5, 10):
    print(get_biggest_decimal_pandigital(i))