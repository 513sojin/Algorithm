from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
com = []

for i in range(1, n+1):
    com += combinations(arr, i)

count = 0
for i in com:
    if sum(i) == s:
        count += 1

print(count)