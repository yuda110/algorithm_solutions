def get_palindrome(range_to):
    result_sum = 0
    for decimal_num in range(range_to):
        binary_num = bin(decimal_num).replace('0b', '')
        if str(decimal_num)== str(decimal_num)[::-1] and str(binary_num)== str(binary_num)[::-1] :
            result_sum += decimal_num
    return result_sum

print(get_palindrome(1000000))