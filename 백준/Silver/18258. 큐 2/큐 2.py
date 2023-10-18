from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque()
for _ in range(n):
    status = input().split()
    if 'push' in status[0]:
        queue.append(status[1])
    elif status[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif status[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif status[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif status[0] == 'size':
        print(len(queue))
    elif status[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)