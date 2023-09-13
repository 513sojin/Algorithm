n,m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
num = []
visited = [False] * n

def backtracking(idx):
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    prev = 0
    for i in range(idx, len(arr)):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            prev = arr[i]
            num.append(arr[i])
            backtracking(i+1)
            visited[i] = False
            num.pop()

backtracking(0)