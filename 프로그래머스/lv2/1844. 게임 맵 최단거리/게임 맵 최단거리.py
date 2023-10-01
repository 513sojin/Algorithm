from collections import deque

def bfs(maps):
    end_y = len(maps)
    end_x = len(maps[0])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    visited = [[0] * end_x for _ in range(end_y)]
    visited[0][0] = 1
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == end_x - 1 and ny == end_y - 1:
                return cnt + 2

            if 0 <= ny < end_y and 0 <= nx < end_x:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = 1
                    queue.append((nx, ny, cnt + 1))
    return -1
    

def solution(maps):
    return bfs(maps)