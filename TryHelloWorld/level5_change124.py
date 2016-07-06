#124 나라의 숫자

from itertools import product

def change124(n):
    count = 1
    digit = 1
    while count != n :
        for i in product('124', repeat=digit):
            cur_num = ''.join(i)
            if count == n :
                break
            count += 1
        digit += 1
    return cur_num

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))