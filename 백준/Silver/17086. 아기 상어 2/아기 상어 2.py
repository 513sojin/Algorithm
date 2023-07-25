import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def bfs(i,j):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((i,j,0))
    visited[i][j] = True

    while queue:
        x,y,cnt = queue.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    return cnt + 1
                else:
                    visited[nx][ny] = True
                    queue.append((nx,ny,cnt + 1))

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result.append(bfs(i,j))

print(max(result))