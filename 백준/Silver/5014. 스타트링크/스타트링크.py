import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int,input().split())
d = [u,-1*d]
visited = {}

def bfs(s):
    visited[s] = 1
    queue = deque()
    queue.append((s,0))

    while queue:
        x,cnt = queue.popleft()

        if x == g:
            return cnt

        for i in d:
            nx = x + i

            if 1 <= nx <= f and nx not in visited:
                visited[nx] = 1
                queue.append((nx, cnt + 1))
    return -1

result = bfs(s)
if result == -1:
    print('use the stairs')
else:
    print(result)
