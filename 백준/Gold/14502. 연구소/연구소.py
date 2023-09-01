import copy
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 벽 만들기, 3개면 bfs
def backtracking(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                backtracking(cnt + 1)
                graph[i][j] = 0

def bfs():
    queue = deque()
    test_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if test_graph[nx][ny] == 0:
                    test_graph[nx][ny] = 2
                    queue.append((nx,ny))

    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 0:
                count += 1
    result = max(result, count)

result = 0
backtracking(0)
print(result)