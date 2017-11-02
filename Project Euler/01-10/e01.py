
# result = 0
# i = 1
#
# while i < 1000 :
#     if i % 3 == 0 or i % 5 == 0:
#         result += i
#     i += 1
#
# print(result)

def get_multiple(n_list):
    sum = 0
    for i in range(1, 1000):
        remainder_list = [i%n for n in n_list]
        if 0 in remainder_list:
            sum += i
    return sum

if __name__ == '__main__':
    n_list = [3, 5]
    sum = get_multiple(n_list)
    print(sum)