import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(set(list(map(int, input().split()))))

arr.sort()
temp = []
def backtracking():
    if len(temp) == m:
        print(*temp)
        return

    for i in range(len(arr)):
        if not temp or temp[-1] <= arr[i]:
            temp.append(arr[i])
            backtracking()
            temp.pop()

backtracking()