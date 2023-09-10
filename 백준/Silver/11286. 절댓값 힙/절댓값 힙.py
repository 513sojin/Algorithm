from queue import PriorityQueue
import sys

input = sys.stdin.readline
q = PriorityQueue()
n = int(input())

for _ in range(n):
    i = int(input())
    if i == 0 and not q.empty():
        print(q.get()[1])
    elif i != 0:
        q.put((abs(i),i))
    else:
        print(0)