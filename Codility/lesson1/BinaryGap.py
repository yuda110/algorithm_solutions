
def solution(n):
    bin_str = bin(n).replace('0b', '')
    bin_gap_list = list(filter(None, bin_str.split('1')))
    if bin_str[-1] == '0':
        bin_gap_list.pop()
    if bin_gap_list:
        max_bin_gap = len(max(bin_gap_list, key=len))
    else:
        max_bin_gap = 0

    return max_bin_gap

if __name__ == '__main__':
    result = solution(100)
    print(result)