import sys
sys.setrecursionlimit(10000)
count = 0
def seperate(words):
    global count

    if words == "":
        return
    
    first = words[0]
    same, diff = 1, 0

    for idx, word in enumerate(words[1:]):
        if same == diff:
            count += 1
            seperate(words[idx + 1:])
            return
        
        if word == first:
            same += 1
        else:
            diff += 1
    
    count += 1
    return
    
def solution(s):
    global count
    seperate(s)
    return count