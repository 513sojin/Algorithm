import sys
from collections import deque
input = sys.stdin.readline

temp = int(input())
for _ in range(temp):
    n = int(input())
    alp = list(input().split())
    queue = deque()

    for a in alp:
        if queue:
            if ord(a) <= ord(queue[0]):
                queue.appendleft(a)
            else:
                queue.append(a)
        else:
            queue.append(a)

    str = ''
    for q in queue:
        str += q
    print(str)