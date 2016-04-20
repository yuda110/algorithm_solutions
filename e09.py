import time

def is_pita(a, b, c) :
    if(a*a + b*b == c*c) :
        return True
    else :
        return False

#21seconds
#def find_pita() :
#    for c in range(3, 1000) :
#        for b in range(2, 1000) :
#            for a in range(1, 1000) :
#                if  a<b and b<c and is_pita(a, b, c) :
#                    if a+b+c == 1000 :
#                        return a*b*c

# 7.97seconds > without c for loop 0.08
def find_pita() :
    for a in range(1, 1000) :
        for b in range(a+1, 1000) :
            c = 1000 - a - b
            if a+b+c == 1000  :
                if  is_pita(a, b, c):
                    return a*b*c

start_time = time.time()
print(find_pita())
print("--- %s seconds ---" % (time.time() - start_time))