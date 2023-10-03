def solution(record):
    answer = []
    hash = {}

    for info in record:
        temp = info.split()
        status, uid = temp[0], temp[1]

        if status == 'Enter' or status == 'Change':
            hash[uid] = temp[2]

    for info in record:
        temp = info.split()
        status, uid = temp[0], temp[1]

        if status == 'Enter':
            answer.append(hash[uid] + "님이 들어왔습니다.")
        elif status == 'Leave':
            answer.append(hash[uid] + "님이 나갔습니다.")

    return answer