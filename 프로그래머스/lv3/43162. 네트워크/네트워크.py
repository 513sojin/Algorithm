def dfs(i, visited, c):
    visited[i] = 1

    for idx, x in enumerate(c[i]):
        if not visited[idx] and x:
            dfs(idx, visited, c)

    return

def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1

    return answer