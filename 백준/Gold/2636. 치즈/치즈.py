import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

time = 0
ans = []

def bfs():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0,0))
    cnt = 0

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if graph[ny][nx] == 0:
                    queue.append((ny,nx))
                else:
                    graph[ny][nx] = 0
                    cnt += 1
                visited[ny][nx] = 1
    return cnt

while True:
    cnt = bfs()
    if not cnt:
        break
    time += 1
    ans.append(cnt)

print(time)
print(ans[-1])

