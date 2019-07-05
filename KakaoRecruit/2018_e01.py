
def solution(record):
    command_dict = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }
    nickname_dict = {}
    answer = []
    admin_msg_list = []

    for r in record:
        r_list = r.split(' ')
        command = r_list[0]
        uuid = r_list[1]

        if command != 'Leave':
            nickname_dict[uuid] = r_list[2]

        if command != 'Change':     # Enter, Leave
            admin_msg_list.append([uuid, command])

    for m in admin_msg_list:
        answer.append(nickname_dict[m[0]] + command_dict[m[1]])
    return answer


if __name__ == '__main__':
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]
    print(solution(record))
