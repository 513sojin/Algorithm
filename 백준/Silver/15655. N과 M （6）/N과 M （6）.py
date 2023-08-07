import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
ans = []

def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, len(num)):
        if num[i] not in ans:
            ans.append(num[i])
            dfs(i + 1)
            ans.pop()

num.sort()
dfs(0)