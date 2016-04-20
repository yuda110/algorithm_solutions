# 29) 2 ≤ a ≤ 100, 2 ≤ b ≤ 100 a, b를 가지고 만들 수 있는 a**b는 중복을 제외하면 모두 몇 개?

def get_square_set(a_range_to, b_range_to) :
    square_list = set()
    for a in range(2, a_range_to+1) :
        for b in range(2, b_range_to+1) :
            square_list.add(a**b)
    return len(square_list)

print(get_square_set(100, 100))