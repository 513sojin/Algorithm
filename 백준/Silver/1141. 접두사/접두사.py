import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())
arr.sort()

cnt = len(arr)
for i in range(1,len(arr)):
    if arr[i].startswith(arr[i-1]):
        cnt -= 1

print(cnt)