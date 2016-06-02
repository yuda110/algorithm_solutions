def gcdlcm(a, b):
    min_range = min(a, b)+1
    
    for i in reversed(range(min_range)):
        if a % i == 0 and b % i == 0:
            gcd = i
            break

    i = a * b
    while True :
        if i % a == 0 and i % b == 0 :
            lcm = i
            break
        else :
            i += 1
    
    return [gcd, lcm]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))