import sys
input = sys.stdin.readline

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(1,len(arr)):
    arr[i] = arr[i] + arr[i-1]

for i in range(m):
    x,y = list(map(int, input().split()))

    if x > 1:
        print(arr[y-1]- arr[x-2])
    else:
        print(arr[y-1])