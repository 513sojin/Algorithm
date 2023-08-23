import sys
input = sys.stdin.readline
k = int(input())

dp = [[0,0] for _ in range(46)]

dp[1] = [0,1]
dp[2] = [1,1]
dp[3] = [1,2]

if k <= 3:
    print(dp[k][0], dp[k][1])
else:
    for i in range(4,k+1):
        dp[i] = [dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1]]
    print(dp[k][0], dp[k][1])