import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
dist = [[-1] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int, input().strip())))

def bfs(a,b):
    queue = deque()
    queue.append((a,b))

    dist[0][0] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    if graph[nx][ny] == 1:
                        dist[nx][ny] = dist[x][y]
                        queue.appendleft((nx,ny))
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx,ny))

bfs(0,0)
print(dist[n-1][n-1])
