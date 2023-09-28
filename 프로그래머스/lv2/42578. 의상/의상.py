def solution(clothes):
    hash = {}

    for i in clothes:
        if i[1] in hash:
            hash[i[1]] += 1
        else:
            hash[i[1]] = 1

    answer = 1
    for i in hash.values():
        answer *= (1+ i)
    
    return answer -1