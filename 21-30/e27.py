#python3
# n2 + an + b (단 | a | < 1000, | b | < 1000)
# 연속된 n에 대해 가장 많은 소수를 만들어내는 2차식을 찾아 a*b를 구해라
import cProfile

def is_prime_num(num) :
    if num <= 1  : return False
    for i in range(2, int(num**0.5) + 1):
        if num % i==0:
            return False
    return True

def is_eular_2cha(n,a=1,b=41):
    for n in range(0, n) :
        if is_prime_num(n**2 + a*n + b)  == False:
            return False
    return True

# 오일러 계수 a와 b return
def get_euler_a_b(a, b):
    max_n = 0
    result_a = 0
    result_b = 0
    for aa in range(-a, a):
        for bb in range(-b, b):
            n = 0
            while True :
                if is_eular_2cha(n, aa, bb) == True :
                    if n > max_n :
                        max_n = n
                        result_a = aa
                        result_b = bb
                    n += 1
                else :
                    break
    return result_a, result_b

#cProfile.run('get_euler_a_b(1000, 1000)')
a, b = get_euler_a_b(1000, 1000)
print(a*b)