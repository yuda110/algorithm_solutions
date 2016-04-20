def is_devidable(num_todo, num_to_devide):
    return num_todo % num_to_devide == 0

def is_devidable_at_range(num_todo,range_from, range_to ):
    result = True
    for i in range(range_from, range_to):
        if not is_devidable(num_todo, i):
            result = False
            break
    return result

def find_devidable_min_value(range_from, range_to) :
    num_todo = range_to
    while True :
        if num_todo % range_to == 0 :
            if not is_devidable_at_range(num_todo, range_from, range_to) :
                print(num_todo)
            else :
                break
        num_todo += range_to
    return num_todo

print(find_devidable_min_value(1, 20))