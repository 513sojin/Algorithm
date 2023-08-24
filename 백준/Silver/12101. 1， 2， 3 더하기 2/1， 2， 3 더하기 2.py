import sys
input = sys.stdin.readline
n,k = map(int , input().split())

cnt = 0
arr = []
num = [1,2,3]

def dfs():
    global cnt
    if sum(arr) == n:
        cnt += 1
        if cnt == k:
            print('+'.join(map(str, arr)))
            exit()
        return
    elif sum(arr) > n:
        return

    for i in range(len(num)):
        arr.append(num[i])
        dfs()
        arr.pop()

dfs()
print(-1)
