def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    return n - len(lost)