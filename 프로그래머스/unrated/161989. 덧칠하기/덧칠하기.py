def solution(n, m, section):
    answer = 0
    
    temp = 0
    for s in section:
        if s < temp:
            continue 
            
        temp = s + m
        answer += 1
                
    return answer