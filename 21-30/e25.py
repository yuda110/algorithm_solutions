#python3
def cal_fibo(digit) :
    num1 = 1
    num2 = 1
    seq = 3
    while True :
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if len(str(num3)) >= digit :
            return seq
        seq += 1

print(cal_fibo(1000))