#python3
import re

def cal_unit_fraction(denominator) :
    return re.findall('.(\d+)', str(1/denominator))

def cal_recurring_cycle(deno) :
    num_list = cal_unit_fraction(deno)
    int(num_list[0])
    for num in num_list :
        print(num)

cal_recurring_cycle(8)