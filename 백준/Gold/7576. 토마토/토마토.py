from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split()) #가로 세로
graph = [list(map(int, input().split())) for _ in range(n)]

#상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

queue = deque()
result = 0  # 며칠만에 익는지
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j,0))

while queue:
    x, y, cnt = queue.popleft()
    result = cnt
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            queue.append((nx, ny, cnt + 1))

for item in graph:
    if 0 in item:
        result = -1

print(result)
