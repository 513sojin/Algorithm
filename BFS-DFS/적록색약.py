from collections import deque

n = int(input())
graph = []

for i in range(n):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

green = 0  # 적록색약
not_green = 0  # 적록색약 아닌 사람

visited = [[0] * n for _ in range(n)]

def bfs(x, y, is_green_blind):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for idx, _ in enumerate(dx):

            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if is_green_blind:
                    if ((graph[x][y] == "R" or graph[x][y] == "G") and graph[nx][ny] == "B") or (graph[x][y] == "B" and (graph[nx][ny] == "R" or graph[nx][ny] == "G")):
                        continue
                else:
                    if graph[nx][ny] != graph[x][y]:
                        continue

                queue.append((nx, ny))
                visited[nx][ny] = 1
    return True


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, False)
            green += 1

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, True)
            not_green += 1

print(green, not_green)

# 총평
# 0,1로 이뤄진 graph가 아니라면 방문여부를 담는 리스트가 있는게 좋아보인다.