import heapq
import sys

input = sys.stdin.readline
n = int(input())
q = []
result = []

for i in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(q, x)
    else:
        if q:
            r = heapq.heappop(q)
            result.append(r)
        else:
            result.append(0)


for i in result:
    print(i)