import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k,t,m = map(int, input().split())
    score = [[0 for _ in range(k)] for _ in range(n)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]

    for idx in range(m):
        i,j,s = map(int,input().split())
        score[i-1][j-1] = max(score[i-1][j-1], s)
        submit[i-1] += 1
        time[i-1] = idx

    result = []
    for i in range(n):
        result.append((sum(score[i]), submit[i], time[i], i))

    result.sort(key=lambda x: (-x[0], x[1], x[2]))

    for rank in range(n):
        if result[rank][3] == t - 1:
            print(rank + 1)