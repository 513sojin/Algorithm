def solution(keymap, targets):
    answer = []
    alp = {}
    
    for k in keymap:
        for idx, val in enumerate(k):
            if val in alp and alp[val] < idx + 1:
                continue
            alp[val] = idx + 1
            
    for t in targets:
        temp = 0
        for i in t:
            if i in alp:
                temp += alp[i]
            else:
                temp = -1
                break
        answer.append(temp)
    return answer