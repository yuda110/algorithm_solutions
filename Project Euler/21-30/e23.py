#python3
#자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
#예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
#또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 초과수라고 합니다.

#12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 초과수 중에서는 가장 작습니다.
#따라서 초과수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

#해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 초과수의 합으로 표현 가능함을 보일 수가 있습니다.
#두 초과수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는 더 이상 이 한계값을 낮출 수 없다고 합니다.

#그렇다면, 초과수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?

import time

limit = 28123

def get_divisors(num) : 
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors += [i, num/i]
    divisors.remove(num)
    divisors.sort()
    return sum(sorted(list(set(divisors))))

def is_abundant_number(num) :
    if get_divisors(num) > num :
        return True
    else :
        return False

def sum_cannot_be_written_as_the_sum(limit) :
    sum_result = set()
    abundant_list = [n for n in range(12, limit) if is_abundant_number(n)]
    for i in abundant_list :
        for j in abundant_list :
            if i+j < limit :
                sum_result.add(i+j)
    return sum_result

start_time = time.time()
print(sum(range(1, limit))-sum(sum_cannot_be_written_as_the_sum(limit)))
print("--- %s seconds ---" % (time.time() - start_time))