def solution(score):
    result = [sum(n) / 2 for n in score]
    arr = sorted(result, reverse = True)
    answer = [arr.index(i) + 1 for i in result]
    return answer