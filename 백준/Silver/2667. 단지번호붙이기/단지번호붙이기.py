import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]


ans = []
visited = [[0] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

total = 0

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    count = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    queue.append((ny, nx))
                    count += 1
                    visited[ny][nx] = 1

    return count


for y in range(n):
    for x in range(n):
        if not visited[y][x] and graph[y][x] == 1:
            ans.append(bfs(y, x))
            total += 1

ans.sort()
ans = [total] + ans
for a in ans:
    print(a)
