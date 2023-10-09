from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
queue = deque()

result = 0

for arr in array:
    if len(arr) == 1:
        if queue:
            i, score, time = queue.popleft()
            if time - 1 == 0:
                result += score
            else:
                queue.appendleft((i,score,time - 1))
    else:
        if arr[2] - 1 == 0:
            result += arr[1]
            continue
        queue.appendleft((arr[0],arr[1],arr[2]-1))

print(result)