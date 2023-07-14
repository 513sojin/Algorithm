from collections import deque

n, m, k = map(int, input().split()) # 세로 가로
graph = [[0] * (m) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]
result = []

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1
    count = 1

    while queue:
        i, j = queue.popleft()

        for idx, _ in enumerate(dx):
            x = dx[idx] + i
            y = dy[idx] + j

            if 0 <= x < n and 0 <= y < m:
                if visited[x][y] == 0 and graph[x][y] == 1:
                    queue.append([x,y])
                    count += 1
                    visited[x][y] = 1
    return count


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            result.append(bfs(i,j))

print(max(result))