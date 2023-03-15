from collections import  deque

n, m = map(int, input().split())

graph = []
count = 0
result = 0

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()

        # 실행조건
        for idx, val in enumerate(dx):
            nx = x + dx[idx]
            ny = y + dy[idx]

            # 범위 안일때
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                else:
                    continue
            # 범위 밖
            else:
                continue
    return graph[n-1][m-1]

print(bfs(0,0))