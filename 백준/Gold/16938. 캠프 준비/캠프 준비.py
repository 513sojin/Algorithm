import sys
input = sys.stdin.readline
from itertools import combinations

n,l,r,x = map(int , input().split())
score = list(map(int, input().split()))
cnt = 0
result = []
result.sort()
for i in range(2, n+1):
    result.extend(list(combinations(score,i)))

for item in result:
    if l <= sum(item) <= r and max(item) - min(item) >= x:
        cnt += 1

print(cnt)