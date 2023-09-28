def solution(nums):
    answer = 0
    s = set()
    n = len(nums)
    
    for i in nums:
        s.add(i)
        
    if len(s) <= n//2:
        return len(s)
    
    return n//2