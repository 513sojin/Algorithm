from collections import  deque

a,b = map(int, input().split())
graph = []
count = 0

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(a):
    graph.append(list(input()))


def bfs(start_x, start_y):
    queue = deque([[start_x, start_y]])
    graph[start_x][start_y] = "1"

    while queue:
        x, y = queue.popleft()

        for idx, val in enumerate(dx):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < a and nx >= 0 and ny < b and ny >= 0:
                if graph[nx][ny] == "0":
                    queue.append([nx, ny])
                    graph[nx][ny] = "1"
    return True

# 작성 못했던 부분
for i in range(a):
    for j in range(b):
        if graph[i][j] == "0":
            bfs(i, j)
            count += 1

print(count)

# 1. 끝나는 시점을 아는 방법 ..?
#   bfs 를 사용했을 때는 bfs 함수를 나왔을 때임
# 2. 시작점 어디로 넣어야함 ?
#   for 문을 돌면서 찾아보아요
