#소수구하는 모듈인 primesieve로 일단 구함. 그중에 고름
#순환소수인지 판별할 때는 순열조합 모듈인 itertools.permutations를 사용

import primesieve

def is_circular_prime(num):
   for 검사해야할num in permutations(str(num)):
      검사해야할num = int(''.join(검사해야할num))
      if 검사해야할num == 소수:
         result = True
      else :
         result = False
   return result
   
def get_circular_prime(range_to):
   count = 0
   prime_list = generate_프라임(range_to)      #[2, 3, 5, 7, 11, 13, 17, 19....]
   for prime in prime_list:
      if is_circular_prime(prime) == 'True':
         count += 1
   return count