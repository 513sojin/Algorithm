def solution(s, skip, index):
    answer = ''
    skip_alp = {}
    
    for temp in skip:
        skip_alp[temp] = True
    
    for alp in s:
        count = index
        temp = ord(alp)
        while count != 0:
            temp += 1
            
            if temp > ord('z'):
                temp = temp - ord('z') + ord('a') - 1
            
            if chr(temp) in skip_alp:
                continue
            count -= 1
        answer += chr(temp)
    
    return answer