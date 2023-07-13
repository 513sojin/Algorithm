from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
    visited = [0] * (n + 1)
    num = [0] * (n + 1)
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                num[i] = num[v] + 1
    return sum(num)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)
