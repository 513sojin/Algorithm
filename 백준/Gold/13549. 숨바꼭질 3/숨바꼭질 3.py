from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
visited = [False] * MAX

def bfs(point):
    queue = deque()
    queue.append((point, 0))
    visited[point] = True

    while queue:
        n, time = queue.popleft()

        if n == k:
            return time
        else:
            if 0 <= 2*n < MAX and not visited[n*2]:
                queue.append((n*2, time))
                visited[n*2] = True
            if 0 <= n - 1 < MAX and not visited[n-1]:
                queue.append((n-1, time + 1))
                visited[n-1] = True
            if 0 <= n + 1 < MAX and not visited[n+1]:
                queue.append((n + 1, time + 1))
                visited[n+1] = True

print(bfs(n))