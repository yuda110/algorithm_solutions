"""
무지의 먹방 라이브
"""


# fail to pass 30, 31
def solution(food_times, k):
    time_idx_list = [(t, idx) for idx, t in enumerate(food_times)]
    answer = -1

    for i in range(len(food_times)):
        if not time_idx_list:
            break
        elif len(time_idx_list) > k:
            answer = time_idx_list[k][1] + 1
            break
        else:
            k -= len(time_idx_list)
            time_idx_list = [(ti[0]-1, ti[1]) for ti in time_idx_list if ti[0]-1 > 0]

    return answer


if __name__ == '__main__':
    # solution([3, 1, 2, 1, 4], 7)    # 5
    # solution([3, 1, 2], 5)      # 1
    # solution([1, 1, 1], 7)  # -1
    solution([5, 6, 2, 5, 2], 14)   # 2