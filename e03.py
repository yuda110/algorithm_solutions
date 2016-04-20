#prime_list = []
last_prime = 0

def prime_factor(target) :
    i = 2
    while target != 1 :
        while target % i == 0 :
            last_prime = i
            #prime_list.append(i)
            target = target / i
        if target == 1 :
            break
        i += 1
    return last_prime

prime_result = prime_factor(600851475143)
print(prime_result)
#print(max(prime_result))