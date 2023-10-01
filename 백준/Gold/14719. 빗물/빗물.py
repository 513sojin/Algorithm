import sys
input = sys.stdin.readline

h,w = map(int, input().split())
arr = list(map(int ,input().split()))

graph = [[0]*w for _ in range(h)]
result = []

for idx, a in enumerate(arr):
    for j in range(a):
        graph[j][idx] = 1

for i in graph:
    flag = False
    cnt = 0
    prev = i[0]
    for j in i:
        if not flag and j == 1: # 1이 없었는데 현재 값이 1이라면
            flag = True
        elif flag and j == 0: # flag true, 현재 0
            cnt += 1
        elif flag and j == 1: #flag true, 현재 1
            if prev == 1 and flag:
                continue
            result.append(cnt)
            cnt = 0
        prev = j

print(sum(result))