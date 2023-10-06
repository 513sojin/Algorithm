from collections import deque
def bfs(start, end, graph, w, h):     
    visited = [[0]* w for _ in range(h)]
    
    queue = deque([(start[0], start[1], 0)])
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    while queue:
        y, x, cnt = queue.popleft()
        
        if (y,x) == end:
            return cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and graph[ny][nx] != 'X':
                    visited[ny][nx] = 1
                    queue.append((ny,nx,cnt + 1))
    return -1   

def solution(maps):
    answer = 0
    h = len(maps)
    w = len(maps[0])
    
    graph = [[0]*w for _ in range(h)]
    
    start = ()
    end = ()
    lever = ()
    
    for y, m in enumerate(maps):
        for x, val in enumerate(m):
            graph[y][x] = val
            if val == 'S':
                start = (y,x)
            elif val == 'E':
                end = (y,x)
            elif val == 'L':
                lever = (y,x)
                
    first_result = bfs(start, lever, graph, w, h)
    second_result = bfs(lever, end, graph ,w,h)
    
    if first_result == -1 or second_result == -1:
        return -1
    else:
        return first_result + second_result