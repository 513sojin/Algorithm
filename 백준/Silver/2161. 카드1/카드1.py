from collections import deque

n = int(input())
queue = deque()
result = []

for i in range(1, n + 1):
    queue.append(i)

while len(queue) > 1:
    result.append(queue.popleft())

    if len(queue) > 1:
        queue.append(queue.popleft())
result.append(queue.pop())

print(' '.join(map(str, result)))