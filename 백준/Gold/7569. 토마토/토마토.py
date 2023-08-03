import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]


cnt = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append((x,y,z,0))
            elif graph[z][y][x] == 0:
                cnt += 1

if cnt == 0:
    print(0)
else:
    result = 0

    while queue:
        x, y, z, cnt = queue.popleft() # 세로 가로
        result = cnt

        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and not graph[nz][ny][nx]:  # 세로 가로
                if graph[nz][ny][nx] == -1:
                    continue
                graph[nz][ny][nx] = 1
                queue.append((nx, ny, nz, cnt + 1))

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:
                    print(-1)
                    exit()

    print(result)