import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x:x[0])
heap = []
answer = 1

for start,end in arr:
    if heap:
        num = heapq.heappop(heap)
        if num > start:
            answer += 1
            heapq.heappush(heap, num)
        heapq.heappush(heap, end)
    else:
        heapq.heappush(heap, end)
print(answer)