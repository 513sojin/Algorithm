from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
cnt = 0

def bfs(point):
    global cnt
    global result
    queue = deque()
    queue.append((point, 0))
    visited[point] = 0

    while queue:
        n, time = queue.popleft()

        if n == k:
            cnt += 1
        else:
            if 0 <= 2*n < MAX and (visited[n*2] == -1 or visited[n*2] == visited[n] + 1):
                queue.append((n*2, time + 1))
                visited[n*2] = time + 1
            if 0 <= n - 1 < MAX and (visited[n-1] == -1 or visited[n-1] == visited[n] + 1):
                queue.append((n-1, time + 1))
                visited[n-1] = time + 1
            if 0 <= n + 1 < MAX and (visited[n+1] == -1 or visited[n+1] == visited[n] + 1):
                queue.append((n + 1, time + 1))
                visited[n+1] = time + 1

bfs(n)
print(visited[k])
print(cnt)