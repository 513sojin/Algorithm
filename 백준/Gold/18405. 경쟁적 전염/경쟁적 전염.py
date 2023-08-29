import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
sort_graph = []
queue = deque()

for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

for b in range(n):
    for a in range(n):
        if graph[b][a] != 0:
            sort_graph.append((graph[b][a], b, a))

sort_graph.sort(key= lambda x: x[0])

for item in sort_graph:
    queue.append((item[1], item[2], 0))

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
    while queue:
        y, x, cnt = queue.popleft()

        if cnt >= s:
            return

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
                queue.append((ny, nx, cnt + 1))
                graph[ny][nx] = graph[y][x]

bfs()
print(graph[x-1][y-1])