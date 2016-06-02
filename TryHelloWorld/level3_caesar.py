import string

def cal_caesar(alp, n):
    caesar_alp_num = string.ascii_uppercase.index(alp.upper()) + n
    if caesar_alp_num > 26 : caesar_alp_num -= 26
    return caesar_alp_num

def caesar(s, n):
    result_list = []
    alp_list = s.split()
    for alp in alp_list:
        if alp.isupper() :
            result_list.append(string.ascii_uppercase[cal_caesar(alp, n)])
        else :
            result_list.append(string.ascii_lowercase[cal_caesar(alp, n)])
    result = '"'+' '.join(result_list)+'"'
    return result


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))