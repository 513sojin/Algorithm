import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
result = 0
ans = []

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs(i, j):
    graph[i][j] = 0

    queue = deque()
    queue.append((i, j))
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((ny, nx))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(i,j))
            result += 1

print(result)
ans.sort()
for a in ans:
    print(a)