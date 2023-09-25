import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(start, graph):
    queue = deque()
    queue.append((start[0], start[1]))

    while queue:
        x,y = queue.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            print("happy")
            return

        for idx, val in enumerate(graph):
            if not visited[idx] and abs(val[0] - x) + abs(val[1] - y) <= 1000:
                queue.append((val[0], val[1]))
                visited[idx] = 1
    print("sad")

for _ in range(t):
    c = int(input())
    graph = deque()
    start = list(map(int,input().split()))

    for _ in range(c):
        x, y = map(int, input().split())
        graph.append((x,y))
    end = list(map(int,input().split()))

    visited = [0 for _ in range(c)]
    bfs(start, graph)