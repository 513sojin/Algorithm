def solution(park, routes):
    h = len(park)
    w = len(park[0])

    graph = [[0] * w for _ in range(h)]
    start = []

    for i, p in enumerate(park):
        for j, val in enumerate(p):
            graph[i][j] = val
            if val == 'S':
                start = [i, j]

    y, x = start[0], start[1]
    d = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}

    for r in routes:
        direction, step = r.split()

        nx, ny = 0,0
        for _ in range(int(step)):
            nx += d[direction][1]
            ny += d[direction][0]

            new_x = x + nx
            new_y = y + ny
            if (0 > new_x or new_x >= w or 0 > new_y or new_y >= h) or graph[new_y][new_x] == 'X':
                nx, ny = 0, 0
                break

        x += nx
        y += ny

    return [y, x]