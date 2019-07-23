import inflect
from py_modules.timer import logging_time


@logging_time
def solution():
    e = inflect.engine()
    result = ''
    for i in range(1, 1001):
        str_i = e.number_to_words(i)
        result += str_i
    result = len(result.replace('-', '').replace(' ', ''))
    return result


@logging_time
def solution2():
    num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
                80: 'eighty', 90: 'ninety', 100: '', 0: '', 1000: 'thousand'}
    result1 = 0
    for i in range(1, 21):
        result1 += len(num_dict[i])
    for i in range(21, 100):
        ten = i//10 * 10
        one = i - ten
        result1 += len(num_dict[ten] + num_dict[one])

    result2 = 0
    for i in range(1, 10):
        result2 += len(num_dict[i] + 'hundred')
        result2 += len(num_dict[i] + 'hundred' 'and')*99 + result1
    result2 += len('onethousand')

    return result1 + result2


if __name__ == '__main__':
    # solution()
    solution2()
