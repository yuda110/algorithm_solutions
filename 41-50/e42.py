import string

text = open('./41-50/words.txt', 'r', encoding='utf-8')

def get_nth_triangle_num(n):
    triangle_num = int(0.5*n*(n+1))
    return triangle_num

def if_alp_triangle_num(alp_string):
    triangle_num, cnt = 0, 1
    result_sum = sum([string.ascii_uppercase.index(i)+1 for i in list(alp_string)])
    while triangle_num <= result_sum :
        triangle_num = get_nth_triangle_num(cnt)
        if result_sum == triangle_num :
            return True
        else :
            cnt += 1
    return False
    
def get_num_of_triangle_num_of_words():
    result_true = 0
    words = text.readline()
    for word in words.split(','):
        alp_string = word.replace('"', '').replace('"', '')
        if if_alp_triangle_num(alp_string) == True:
            result_true += 1
    return result_true

print(get_num_of_triangle_num_of_words())