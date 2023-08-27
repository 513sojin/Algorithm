import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip().split('.')[1])

arr = Counter(arr)

for key, value in sorted(arr.items()):
    print(key, value)