from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = 0

for per in permutations(arr):
    temp = 0
    for i in range(n-1):
        temp += abs(per[i] - per[i+1])
    result = max(result, temp)
print(result)