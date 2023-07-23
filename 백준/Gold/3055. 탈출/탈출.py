from collections import deque
import sys

r,c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

sx = 0
sy = 0

wqueue = deque()

def waterSpread():
    for _ in range(len(wqueue)):
        x,y = wqueue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                wqueue.append((nx,ny))
                visited[nx][ny] = True

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            sx, sy = i, j
            graph[i][j] = '.'
        if graph[i][j] == '*':
            wqueue.append((i,j))

def bfs(x, y):
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = True

    while queue:
        waterSpread()

        for _ in range(len(queue)):
            x, y, cnt = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '*' and graph[nx][ny] != 'X':
                    if graph[nx][ny] == '.':
                        queue.append((nx, ny, cnt + 1))
                        visited[nx][ny] = True
                    elif graph[nx][ny] == 'D':
                        return cnt + 1

    return "KAKTUS"

print(bfs(sx, sy))