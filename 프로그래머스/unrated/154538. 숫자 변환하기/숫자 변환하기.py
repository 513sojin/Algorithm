from collections import deque 

def bfs(x,y,n):
    MAX = 1000001
    queue = deque([(x, 0)])
    visited = set()
    
    while queue:
        dx, cnt = queue.popleft()
        
        if dx == y:
            return cnt
        
        for i in [dx + n, dx * 2, dx * 3]:
            nx = i
            
            if nx <= MAX and not nx in visited:
                queue.append((nx, cnt + 1))
                visited.add(nx)
    return -1
    
def solution(x, y, n):
    return bfs(x,y,n)