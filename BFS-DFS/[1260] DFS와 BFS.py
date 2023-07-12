from collections import deque
n, m, v = map(int, input().split())

#노드가 주어진 경우 인접행렬을 만들어보자
matrix = [[0]*(n+1) for i in range(n+1)]

visited_d = [0] * (n+1)
visited_b = [0] * (n+1)

for i in range(m):
  a, b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    visited_d[v] = 1
    print(v, end=" ")

    for i in range(n+1):
        if visited_d[i] == 0 and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_b[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(n+1):
            if visited_b[i] == 0 and matrix[v][i] == 1:
                queue.append(i)
                visited_b[i] = 1

dfs(v)
print()
bfs(v)