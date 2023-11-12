import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
numbers = [input().strip() for _ in range(n)]
result = set()

for item in permutations(numbers, k):
    result.add(''.join(map(str, item)))

print(len(result))