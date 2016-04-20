#분자 numerator / 분모 denominator

exception_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def make_fraction_list():
    fraction_list = []
    for nume in range(11, 98):
        for deno in range(10, 98):
            if nume <= deno or nume in exception_list or deno in exception_list:
                pass
            else :
                nume_list = list(str(nume))
                deno_list = list(str(deno))
                for num in nume_list:
                    if num in deno_list and num != '0':
                        overlap_num = num
                        fraction_list.append([nume, deno, overlap_num])
    return fraction_list

print(make_fraction_list())