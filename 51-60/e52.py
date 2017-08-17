
def get_smallest_num():
    num = 1
    while True:
        num_list = sorted(list(str(num)))
        for i in range(6, 1, -1):
            multiplied_num_list = sorted(list(str(num*i)))
            if num_list != multiplied_num_list:
                num += 1
                break
            elif i == 2:
                return num

if __name__ == '__main__':
    print(get_smallest_num())
