
# result = 0
# i = 1
#
# while i < 1000 :
#     if i % 3 == 0 or i % 5 == 0:
#         result += i
#     i += 1
#
# print(result)

# def get_multiple(n_list):
#     sum = 0
#     for i in range(1, 1000):
#         remainder_list = [i%n for n in n_list]
#         if 0 in remainder_list:
#             sum += i
#     return sum

# if __name__ == '__main__':
#     n_list = [3, 5]
#     sum = get_multiple(n_list)
#     print(sum)


# n = 1000
# a = ((n-1)//3)
# b = ((n-1)//5)
# c = ((n-1)//15)
# sum = (((3 * a * (a+1))//2) + ((5 * b * (b+1))//2) - ((15 * c * (c+1))//2))
# print(int(sum))


def foo(num):
    return sum([i for i in range(1, num+1) if i % 3 == 0 or i % 5 == 0])


if __name__ == '__main__':
    result = foo(1000)
    print(result)

