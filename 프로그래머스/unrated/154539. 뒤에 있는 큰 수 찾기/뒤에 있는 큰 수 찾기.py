def solution(numbers):
    answer = [-1] * len(numbers)
    temp = []
    
    for idx, n in enumerate(numbers):
        while temp and temp[-1][1] < n:
            t = temp[-1]
            answer[t[0]] = n
            temp.pop()
        temp.append((idx, n))
    
    return answer