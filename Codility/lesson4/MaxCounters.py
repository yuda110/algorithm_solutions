# N개의 counter 가 주어지는데 이들은 0으로 세팅되어 있다.
# increase(X): counter X를 1 증가시킴
# max counter: 모든 counter 를 최댓값으로 세팅

def solution(N, A):
    c_list = [0]*N
    max_c = 0
    for val in A:
        if 1 <= val <= N:
            c_list[val - 1] += 1
            curr_c = c_list[val - 1]
            if curr_c > max_c:
                max_c = curr_c
        elif val == N + 1:
            c_list = [max_c]*N
    return c_list


if __name__ == '__main__':
    # result = solution(5, [3, 4, 4, 6, 1, 4, 4])
    result = solution(1, [2, 1, 1, 2, 1])
    print(result)