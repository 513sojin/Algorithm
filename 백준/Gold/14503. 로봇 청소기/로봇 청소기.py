from collections import deque
n,m = map(int, input().split())
r,c,d = map(int, input().split())
cleaned_map = [[0] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

cnt = 0
def bfs(i,j,d):
    global cnt
    queue.append((i,j))
    cleaned_map[i][j] = 1
    cnt += 1

    while queue:
        x, y = queue.popleft()
        flag = 0

        for i in range(4):
            d = (d+3) % 4
            nx = dx[d] + x
            ny = dy[d] + y

            if 0 <= nx < n and 0 <= ny < m:
                if cleaned_map[nx][ny] == 0 and graph[nx][ny] == 0:
                    cleaned_map[nx][ny] = 1
                    queue.append((nx,ny))
                    cnt += 1
                    flag = 1
                    break

        # 주변 칸이 모두 청소된 경우
        if flag == 0:
            if graph[x - dx[d]][y - dy[d]] == 1:
                print(cnt)
                break
            else:
                queue.append((x - dx[d], y - dy[d]))

bfs(r,c,d)