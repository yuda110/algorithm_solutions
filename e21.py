import time

# splitter.py
def d(num) :
    factors = set([1, num])
    for i in range(2, num) :
        if i in factors :
            return int(sum(factors)-num)
        elif num % i == 0 :
            factors.add(i)
            factors.add(num/i)
    return int(sum(factors)-num)

def sum_amicable_numbers(range_to) :
    sum_ami = 0

    for a in range(2, range_to) :
        b = d(a)
        if a == d(b) and a != b :
            sum_ami += a
    return sum_ami

start_time = time.time()
print(sum_amicable_numbers(10000))
print("--- %s seconds ---" % (time.time() - start_time))