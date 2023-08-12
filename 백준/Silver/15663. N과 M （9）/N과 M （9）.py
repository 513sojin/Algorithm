import sys
input = sys.stdin.readline
n,m = map(int , input().split())

num = list(map(int, input().split()))
ans = []
visited = [False] * (n+1)

def dfs():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    prev = 0
    for i in range(len(num)):
        if not visited[i] and prev != num[i]:
            visited[i] = True
            prev = num[i]
            ans.append(num[i])
            dfs()
            visited[i] = False
            ans.pop()

num.sort()
dfs()