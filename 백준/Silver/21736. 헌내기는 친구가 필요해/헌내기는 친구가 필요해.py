from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

#상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    cnt = 0
    queue = deque()
    queue.append((i,j))
    # 세로 가로 카운트

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 'X':
                continue

            if graph[nx][ny] == 'P':
                cnt += 1

            graph[nx][ny] = 'X'
            queue.append((nx, ny))
    return cnt

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            result = bfs(i,j)

if result == 0:
    print("TT")
else:
    print(result)