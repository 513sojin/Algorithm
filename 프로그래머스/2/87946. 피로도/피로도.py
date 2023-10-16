from itertools import permutations

def solution(k, dungeons):
    answer = 0
    temp = k
    
    for per in permutations(dungeons):
        sum = 0
        k = temp
        for min_p, c_p in per:
            if k >= min_p:
                sum += 1
                k -= c_p
        answer = max(answer, sum)
    
    return answer