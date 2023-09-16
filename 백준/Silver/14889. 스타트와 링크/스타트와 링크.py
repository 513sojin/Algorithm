import sys

input = sys.stdin.readline
n = int(input())
arr = [x for x in range(1,n+1)]
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * (n+1)
result = sys.maxsize

def backtracking(idx, cnt):
    global result
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        result = min(result, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtracking(i + 1, cnt + 1)
            visited[i] = False

backtracking(0,0)
print(result)