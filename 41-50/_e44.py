from math import sqrt

#Pn = n (3n − 1)/2

def get_pentagon_num(seq):
    p_num = int(seq * (3*seq - 1)/2)
    return p_num

def is_pentagonal(n):
    result = ((sqrt(24*n) + 1) + 1)//6
    return isinstance(result, int)

# if __name__ == '__main__':
#     return None
    # for i in range(1, 11):
    #     pen1 = get_pentagon_num(i)
    #     pen2 = get_pentagon_num(i+1)
    #     print(pen1, pen2, pen2-pen1)
        #두 오각수의 차가 3씩 늘어남
