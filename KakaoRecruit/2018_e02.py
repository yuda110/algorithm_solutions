from py_modules.timer import logging_time


@logging_time
def solution(N, stages):
    answer_dict = {}
    challengers = len(stages)
    for i in range(1, N+1):
        failure = stages.count(i)
        if challengers != 0:
            answer_dict[i] = failure / challengers
            challengers -= failure
        else:
            answer_dict[i] = 0
    return sorted(answer_dict, key=answer_dict.get, reverse=True)


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 3, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4]))
