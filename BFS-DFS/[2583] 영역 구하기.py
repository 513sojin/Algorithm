import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())

graph = [[0 for j in range(n)] for i in range(m)]
visited = [[0 for j in range(n)] for i in range(m)]
count = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = []

for i in range(k):
    a, b, c, d = map(int, input().split())

    for y in range(b, d):
        for x in range(a, c):
            graph[y][x] = 1

def dfs(i, j, cnt):
    graph[i][j] = 1

    for idx, _ in enumerate(dx):
        x = i + dx[idx]
        y = j + dy[idx]

        if 0 <= x < m and 0 <= y < n:
            if graph[x][y] == 0:
                cnt = dfs(x, y, cnt+1)
    return cnt


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count += 1
            result.append(dfs(i,j, 1))

print(count)
print(*sorted(result))