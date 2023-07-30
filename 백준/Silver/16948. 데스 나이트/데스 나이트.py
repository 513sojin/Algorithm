import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False]*n for _ in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs():
    queue = deque()
    queue.append((r1,c1,0))

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if nx == r2 and ny == c2:
                    return cnt + 1

                queue.append((nx,ny,cnt + 1))
                visited[nx][ny] = True
    return -1

print(bfs())