#python3
import re

def is_pandigital(formula):
    nums = list(re.sub('\D', '', formula))
    return all(num in nums for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def get_number_of_cases():
    

#print(is_pandigital('39 × 186 = 7254'))