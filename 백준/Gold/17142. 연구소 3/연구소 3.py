import sys
from collections import deque
n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
birus_graph = []
queue = deque()

result = sys.maxsize
inf = sys.maxsize

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            birus_graph.append((i,j))

visited = [0] * len(birus_graph) # backtracking
def backtracking(idx, cnt):
    global result
    if cnt == m:
        result = min(result, bfs(queue.copy()))
        return

    for i in range(idx, len(birus_graph)):
        queue.append((birus_graph[i][0], birus_graph[i][1], 0))
        backtracking(i+1, cnt+1)
        queue.pop()

def bfs(q):
    visited_graph = [[0]*n for _ in range(n)]
    time = 0
    while q:
        x, y, cnt = q.popleft()
        visited_graph[x][y] = 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if visited_graph[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited_graph[nx][ny] = 1
                    time = max(time, cnt + 1)
                    q.append((nx,ny,time))
                elif visited_graph[nx][ny] == 0 and graph[nx][ny] == 2:
                    visited_graph[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and visited_graph[i][j] == 0:
                return result
    return time

backtracking(0,0)
print(result if result != inf else -1)