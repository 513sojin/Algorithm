import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = [[0]*(n+2) for _ in range(n)]

for i in range(n):
    l = []
    l.append(0)
    l.extend(list(map(int,input().split())))
    l.append(0)

    arr.append(l)

dp[0][1] = arr[0][1]

for i in range(1,n):
    for j in range(1, i+2):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))