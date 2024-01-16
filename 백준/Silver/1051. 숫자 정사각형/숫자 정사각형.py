import sys

input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]

min_num = min(n,m)
size = 1

for i in range(1, min_num):
    for j in range(n):
        if j + i >= n:
            continue
        for k in range(m):
            if k + i >= m:
                continue
            if map[j+i][k+i] == map[j][k] == map[j+i][k] == map[j][k+i]:
                size = i + 1

print(size*size)
