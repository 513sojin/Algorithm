import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * n

for idx, val in enumerate(arr):
    while stack and stack[-1][0] < val:
        tmp, index = stack.pop()
        result[index] = val
    stack.append([val, idx])

print(' '.join(map(str, result)))