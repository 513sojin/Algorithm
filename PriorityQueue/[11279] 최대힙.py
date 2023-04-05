import heapq
import sys

n = int(sys.stdin.readline())
q = []
result = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if q:
            result.append(-1 * heapq.heappop(q))
        else:
            result.append(0)
    else:
        heapq.heappush(q, -1 * x)

for i in result:
    print(i)