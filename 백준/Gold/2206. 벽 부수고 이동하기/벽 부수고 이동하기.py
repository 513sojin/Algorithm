from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
    queue = deque()
    queue.append((0,0,0))

    while queue:
        x, y, cnt = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][cnt]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue

            if graph[nx][ny] == 1 and cnt == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 벽 없고, 벽 안깬 경우
            elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                queue.append((nx, ny, cnt))

    return -1

print(bfs())