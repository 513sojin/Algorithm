from collections import deque
n,m = map(int, input().split())
graph = [0] * 101
visited = [0] * 101

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a] = b

start = 1
def bfs():
    queue = deque()
    queue.append((start, 0))

    while queue:
        x, cnt = queue.popleft()

        if x == 100:
            return cnt

        for i in range(1,7):
            next = i + x

            if next <= 100 and not visited[next]:
                visited[next] = 1

                if graph[next]:
                    queue.append((graph[next], cnt + 1))
                else:
                    queue.append((next, cnt + 1))

print(bfs())