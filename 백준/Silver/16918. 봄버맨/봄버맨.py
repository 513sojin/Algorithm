from collections import deque
r,c,n = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(input()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def put_bomb():
    for i in range(r):
        for j in range(c):
            graph[i][j] = 'O'

def count_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb_graph.append((i,j))

def explodes_bomb():
    while bomb_graph:
        x, y = bomb_graph.popleft()
        graph[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '.':
                graph[nx][ny] = '.'

    return graph

n -= 1
while n:
    bomb_graph = deque()

    count_bomb()
    put_bomb()

    n -= 1
    if n == 0:
        break

    explodes_bomb()
    n -= 1

for i in graph:
    print("".join(i))
