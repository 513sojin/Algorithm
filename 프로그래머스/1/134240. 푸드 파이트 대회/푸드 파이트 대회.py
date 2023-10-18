def solution(food):
    answer = ''
    
    temp = ''
    for idx, f in enumerate(food):
        if idx == 0:
            continue
        temp += str(idx) * (f // 2)
    
    answer = temp + '0' + temp[::-1]
    
    return answer