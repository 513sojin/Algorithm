from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

#상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

graph = [input() for _ in range(n)]

def bfs(i,j):
    queue = deque()
    queue.append((i, j))
    num = [[0] * m for _ in range(n)]
    num[i][j] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for idx, _ in enumerate(dx):
            nx = dx[idx] + x
            ny = dy[idx] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 'W' or num[nx][ny] > 0:
                continue

            num[nx][ny] = num[x][y] + 1
            cnt = max(cnt, num[nx][ny])
            queue.append((nx, ny))
    return cnt - 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i,j))

print(result)
