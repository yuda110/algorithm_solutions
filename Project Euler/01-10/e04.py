"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from py_decorators.timer import logging_time


# def is_palindrome(num):
#     if str(num) == str(num)[::-1]:
#         return True
#     else:
#         return False
#
#
# @logging_time
# def old_get_palindrome(num1, num2):
#     max_palindrome = 0
#     num2_org = num2
#     while num1 > (num1/10):
#         while num2 > (num2/10):
#             multiplied_num = num1*num2
#             if is_palindrome(multiplied_num) and max_palindrome < multiplied_num:
#                 max_palindrome = multiplied_num
#             num2 -= 1
#         num1 -= 1
#         num2 = num2_org
#     return max_palindrome


@logging_time
def get_palindrome(n):
    result = 0
    for i in range(n, 100, -1):
        for j in range(n, 100, -1):
            mul = i*j
            if mul > result and str(mul) == str(mul)[::-1]:
                result = mul
    return result


if __name__ == '__main__':
    print(get_palindrome(999))  # 0.06초 가량

    # 참고로 result 리스트를 append 해서 max 를 뽑아내는 건 0.45초
    # 그리고 old_get_palindrome()는 get_palindrome()의 10배 정도 더 걸린다.
