from collections import deque
a, b = map(int, input().split())

def bfs(a):
    cnt = 1
    queue = deque()
    queue.append((a,0))

    while queue:
        p, cnt = queue.popleft()

        if p > b:
            continue
        elif p == b:
            return cnt
        else:
            queue.append((p * 2, cnt + 1))
            queue.append((int(str(p)+"1"), cnt + 1))
    return -1

result = bfs(a)
if result == -1:
    print(-1)
else:
    print(result + 1)
