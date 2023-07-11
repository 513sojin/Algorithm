import sys
sys.setrecursionlimit(3000000)

n, m = map(int, input().split())

graph = []
count = 0
result = []
# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(i, j,cnt):
    graph[i][j] = 0 # 방문 처리

    for idx, _ in enumerate(dx):
        x = i + dx[idx]
        y = j + dy[idx]

        if 0 <= x < n and 0 <= y < m:
            if graph[x][y] == 1:
                cnt = dfs(x, y, cnt+1)
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += 1
            result.append(dfs(i, j, 1))

print(count)
# 영역이 없을 때의 예외처리가 필요
if len(result) == 0:
    print(0)
else:
    print(max(result))
