"""
#make_arr()로 배열 만들고 아래서부터 위로 큰수 합쳐가는 식으로 계산
아래에서 위로 올라갈 때 작은 삼각형을 만들어 가장 큰 수를 만드는 삼각형을 선택한다.
"""
from py_modules.timer import logging_time


def make_arr(triangle_nums):
    arr = triangle_nums.split('\n')
    new_arr = [i.split(' ') for i in arr]
    return new_arr


@logging_time
def cal_max_sum(num):
    new_arr = make_arr(num)
    i = len(new_arr)-1

    top_num = 0
    while i > 0:
        for j in range(i):
            top_num = int(new_arr[i-1][j])
            left_num = int(new_arr[i][j])
            right_num = int(new_arr[i][j+1])
            if left_num > right_num:
                top_num += left_num
            else:
                top_num += right_num
            new_arr[i-1][j] = top_num
        i -= 1
    return top_num


if __name__ == '__main__':
    triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    cal_max_sum(triangle)
