import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = []

for i in range(m):
    graph.append(list(map(int, input().strip())))

dist = [[-1] * n for _ in range(m)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    dist[0][0] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if dist[nx][ny] == -1: # 방문 안한 경우만
                    if graph[nx][ny] == 0: # 벽이 없는 경우만
                        dist[nx][ny] = dist[x][y]
                        queue.appendleft((nx,ny))
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx,ny))

bfs(0,0)
print(dist[m-1][n-1])