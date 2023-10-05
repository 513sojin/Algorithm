n = int(input())
arr = list(input().split())
temp = []
visited = [0] * 10

def check(n,m,k):
    if k == '>':
        if n < m:
            return False
    else:
        if n > m:
            return False
    return True


def backtracking(idx, num):
    global ans
    if idx == n+1:
        ans.append(num)
        return

    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(num[-1], str(i), arr[idx-1]):
                visited[i] = 1
                backtracking(idx + 1, num + str(i))
                visited[i] = 0

ans = []
backtracking(0, '')
print(ans[-1])
print(ans[0])