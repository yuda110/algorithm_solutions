
def get_palindrome(num1, num2):
    max_palindrome = 0
    num2_org = num2
    while num1 > (num1/10):
        while num2 > (num2/10):
            multiplied_num = num1*num2
            if is_palindrome(multiplied_num) and max_palindrome < multiplied_num:
                max_palindrome = multiplied_num
            num2 -= 1
        num1 -= 1
        num2 = num2_org
    return max_palindrome


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(get_palindrome(9999, 9999))
