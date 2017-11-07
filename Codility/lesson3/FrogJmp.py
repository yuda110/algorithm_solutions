# 작은 개구리 하나가 X에서 Y(혹은 그보다 더 멀리)로 이동하고 싶어한다.
# 개구리는 매 점프마다 D만큼 이동한다.
# 개구리가 원하는 위치에 도달할 때까지 필요한 최소 점프 횟수를 구하라.

def solution(X, Y, D):
    if (Y-X)%D:
        return (Y-X)//D + 1
    else:
        return (Y - X) // D

    # return int(round((Y-X)/D + 0.5))

if __name__ == '__main__':
    print(solution(1, 5, 2))
    print(solution(10, 85, 30))
