def cal_number_of_case(range_to) :
    pre_case = [1]*range_to
    next_case = [1]*range_to
    while pre_case[1] < range_to :
        for i in range(1, range_to) : 
            next_case[i] = next_case[i-1] + pre_case[i]
            pre_case = next_case
    return next_case[-1]

print(cal_number_of_case(21))