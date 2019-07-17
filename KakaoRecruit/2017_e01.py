
def solution(n, arr1, arr2):
    pw_list = [' ', '#']
    result = []
    for i in range(n):
        b = bin(arr1[i] | arr2[i])[2:]
        s = "{:0{}}".format(int(b), n)
        pw = ''.join([pw_list[int(i)] for i in s])
        result.append(pw)
    return result


if __name__ == '__main__':
    # solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
    solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
