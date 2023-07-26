from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
visited = [False] * MAX
moving = [0] * MAX

def bfs(point):
    queue = deque()
    queue.append((point, 0))
    visited[point] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time
        else:
            if 0 <= 2*x < MAX and not visited[x*2]:
                queue.append((x*2, time + 1))
                visited[x*2] = True
                moving[x*2] = x
            if 0 <= x - 1 < MAX and not visited[x-1]:
                queue.append((x-1, time + 1))
                visited[x-1] = True
                moving[x-1] = x
            if 0 <= x + 1 < MAX and not visited[x+1]:
                queue.append((x + 1, time + 1))
                visited[x+1] = True
                moving[x+1] = x

result = bfs(n)
print(result)

ans = []
temp = k
ans.append(k)

for i in range(result):
    ans.append(moving[temp])
    temp = moving[temp]
print(' '.join(map(str, ans[::-1])))