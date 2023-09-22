n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
dict = {0:left, 1:down, 2:right, 3:up}
result = 0

def recount(s_x, s_y, direction):
    global result
    if s_y < 0:
        return

    total = 0
    for dx, dy, z in direction:
        nx = s_x + dx
        ny = s_y + dy
        if z == 0:
            new_sand = graph[s_x][s_y] - total
        else:
            new_sand = int(graph[s_x][s_y] * z)
            total += new_sand

        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] += new_sand
        else:
            result += new_sand

def change_direction():
    x = y = n // 2
    cnt = 1
    move_cnt = 0
    d = 0

    while True:
        move_cnt += 1
        for _ in range(cnt):
            nx = x + dx[d]
            ny = y + dy[d]

            if (ny, nx) == (-1, 0):
                return

            recount(nx,ny,dict[d])
            x,y = nx, ny

        if move_cnt == 2:
            move_cnt = 0
            cnt += 1
        d = (d + 1) % 4

change_direction()
print(result)
