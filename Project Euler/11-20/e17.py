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


# @logging_time
# def solution2():
#     num_list = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
#                 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']


if __name__ == '__main__':
    solution()
