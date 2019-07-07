from itertools import combinations


def is_minimality(k_list, answer):
    for a in answer:
        if all(el in k_list for el in a):  # check minimality
            return False
    return True


def solution(relation):
    answer = []
    zip_r = list(zip(*relation))

    row_len = len(relation)
    col_len = len(relation[0])

    for i in range(1, col_len+1):
        key_set = list(combinations(range(col_len), i))

        for k_list in key_set:
            zipped_tuple = list(zip(*[zip_r[k] for k in k_list]))
            if len(set(zipped_tuple)) == row_len:   # check uniqueness
                if is_minimality(k_list, answer):
                    answer.append(k_list)
    return len(answer)


# def solution(relation):
#     zip_r = list(zip(*relation))
#
#     row_len = len(relation)
#     col_len = len(relation[0])
#
#     case_list = []  # 모든 경우의 수  [(0,), (1,), (2,), ... (0, 1, 2, 3)]
#     for i in range(1, col_len+1):
#         case_list += list(combinations(range(col_len), i))
#
#     unique_list = []     # uniqueness 를 충족하는 경우
#     for case in case_list[:]:
#         zipped_tuple = list(zip(*[zip_r[k] for k in case]))
#         if len(set(zipped_tuple)) == row_len:
#             unique_list.append(case)
#
#     answer = set(unique_list)
#     for i in range(len(unique_list)):
#         for j in range(i+1, len(unique_list)):
#             if all(el in unique_list[j] for el in unique_list[i]):
#                 answer.discard(unique_list[j])
#     return len(answer)


if __name__ == '__main__':
    r = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]
    solution(r)
