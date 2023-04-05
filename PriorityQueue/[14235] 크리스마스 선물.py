import heapq
n = int(input())
q = []
answer = []

for i in range(n):
    x = list(map(int, input().split()))

    if x[0] == 0:
        if q:
            answer.append(-1 * heapq.heappop(q))
        else:
            answer.append(-1)
    else:
        for i in x[1:]:
            heapq.heappush(q, -1 * i)

for i in answer:
    print(i)