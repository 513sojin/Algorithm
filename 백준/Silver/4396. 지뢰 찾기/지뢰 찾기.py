import sys
input = sys.stdin.readline

n = int(input())
bomb = []
graph = []
answer = [['.']*n for _ in range(n)]

flag = False
bomb_location = []

dx = [0,0,-1,1,1,1,-1,-1]
dy = [-1,1,0,0,1,-1,1,-1]

for _ in range(n):
    bomb.append(list(map(str, input().strip())))

for _ in range(n):
    graph.append(list(map(str, input().strip())))

for y in range(n):
    for x in range(n):
        temp = 0
        if graph[y][x] == 'x':
            if bomb[y][x] == '*':
                flag = True
            for k in range(8):
                ny = y + dy[k]
                nx = x + dx[k]

                if 0 <= ny < n and 0 <= nx < n and bomb[ny][nx] == '*':
                    temp += 1
            graph[y][x] = temp
        if bomb[y][x] == '*':
            bomb_location.append((y,x))

if flag:
    for y,x in bomb_location:
        graph[y][x] = '*'

for g in graph:
    print(''.join(map(str, g)))