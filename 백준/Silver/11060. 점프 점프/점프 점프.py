from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
visited = [False] * n

def bfs(i):
    queue = deque()
    queue.append((i, 0))

    while queue:
        i, cnt = queue.popleft() # 위치 (몇번째인지)
        if i == n - 1:
            return cnt

        for j in range(num[i], 0, -1):
            if 0 <= j + i < n and not visited[j+i]:
                if num[j+i] == 0:
                    continue
                queue.append((j + i, cnt + 1))
                visited[j+i] = True
    return -1

print(bfs(0))