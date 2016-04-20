import os
import re

def alphabetize() :
    f = open("C:\\names.txt")
    names = f.readline()
    name_arr = re.findall('\w+', names)
    name_arr.sort()
    return name_arr

def chg_alphabet_to_num() :
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_dict = {}
    seq = 1
    for i in alphabets :
        alpha_dict[i] = seq
        seq += 1
    return alpha_dict

def sum_and_multiple_alphabet_in_name() :
    alpha_dict = chg_alphabet_to_num() 
    name_arr = alphabetize()
    sum_multi_sum = 0
    seq = 1
    for name in name_arr :
        sum = 0
        sum_multi = 0
        for i in name :
            sum += alpha_dict[i]
        sum_multi = sum * (seq)
        sum_multi_sum += sum_multi
        seq += 1
    return sum_multi_sum

print(sum_and_multiple_alphabet_in_name())