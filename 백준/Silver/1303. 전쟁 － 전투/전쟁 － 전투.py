from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j,s):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == s:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

result = [0,0]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            prev = graph[i][j]
            total = bfs(i,j,prev)

            if prev == 'W':
                result[0] += total*total
            else:
                result[1] += total*total

print(result[0], end= ' ')
print(result[1])