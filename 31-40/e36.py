# <<<<<<< HEAD
# def get_binary_num(decimal_num):
# =======
# ﻿def get_binary_num(decimal_num):
# >>>>>>> origin/master
#     binary_num = bin(decimal_num).replace('0b', '')
#     return binary_num

def is_palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1] :
        return  True
    else:
        return False

def get_palindrome(range_to):
    result_sum = 0
    for i in range(range_to):
        decimal_num = i
        binary_num = get_binary_num(decimal_num)
        if is_palindrome(decimal_num)==True and is_palindrome(binary_num)==True :
            result_sum += decimal_num
    return result_sum

print(get_palindrome(1000000))