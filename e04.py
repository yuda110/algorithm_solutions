#-*- coding: utf-8 -*-
#???? ?? ???? ???? > ???ڿ??? ????
#??Ī???? ã?? ?Լ??? ???ڿ??? ????
#while???? ?????? ???ڸ? ?ٿ????? ??Ī???? ????

palindrome = []

def get_palindrome(num1, num2) :
    max_palindrome = 0
    num2_org = num2
    while num1 > (num1/10) :
        while num2 > (num2/10) :
            multipled_num = num1*num2
            if is_palindrome(multipled_num)  and (max_palindrome < multipled_num):
                #if  max_palindrome < num1*num2 :#
                max_palindrome = multipled_num
                #palindrome.append(num1*num2)
            num2 -= 1
        num1 -= 1
        num2 = num2_org
    #return palindrome
    return max_palindrome

def is_palindrome(num) :
    if str(num) == str(num)[::-1] :
        #print("palindrome" + str(num))
        return True
    else :
        return False

#result_list = get_palindrome(99999, 99999)
#print(max(result_list))
print(get_palindrome(9999, 9999))

#max???? ?????ؼ? ????
#m=0
#for i in range(100, 1000):
#    for j in range(100, 1000):
#        k = i * j
#        if str(k) == str(k)[::-1]:
#            if m < k :
#                m = k

#print(m)