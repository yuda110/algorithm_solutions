def is_pandigital(num_list):
    pandigital_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return all(num in num_list for num in pandigital_list)

def cal_formula(range_from, range_to):
    pandigital_result = 0
    for num in range(range_from, range_to):
        n = 1
        result_str = ''
        result_str_list = []
        while len(result_str) < 9 :
            result_num = num*n
            result_str_list.append(str(result_num))
            result_str = ''.join(result_str_list)
            n += 1
        if len(result_str) == 9 :
            result_str_list = list(result_str)
            if is_pandigital(result_str_list)  and int(result_str) > pandigital_result :
                    pandigital_result = int(result_str)
    return pandigital_result

print(cal_formula(2, 9999)) #0.03