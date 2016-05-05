#python3
from fractions import Fraction

exception_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def get_interesting_formula():
    result_fraction = 1
    for nume in range(11, 99):
        for deno in range(10, 98):
            if nume <= deno or nume in exception_list or deno in exception_list:
                pass
            else :
                nume_list = list(str(nume))
                deno_list = list(str(deno))
                for num in nume_list:
                    if num in deno_list and num != '0':
                        overlap_num = num
                        nume_list.remove(overlap_num)
                        interesting_nume = int(nume_list[0])
                        deno_list.remove(overlap_num)
                        interesting_deno = int(deno_list[0])
                        try:
                            if deno/nume == interesting_deno/interesting_nume:
                                result_fraction = result_fraction * interesting_deno/interesting_nume
                        except ZeroDivisionError as e:
                            pass
    result_deno = Fraction(result_fraction).limit_denominator().denominator
    return result_deno

print(get_interesting_formula())