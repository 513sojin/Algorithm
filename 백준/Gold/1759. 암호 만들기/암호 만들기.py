import sys
input = sys.stdin.readline

l,c = map(int, input().split())
arr = list(input().split())

result = []

def check(a):
    v_cnt = 0
    c_cnt = 0

    for i in result:
        if i in ['a','e','i','o','u']:
            v_cnt += 1
        else:
            c_cnt += 1

    if v_cnt >= 1 and c_cnt >= 2:
        return True
    else:
        return False

def dfs(start):
    if len(result) == l:
        if check(result):
            print(''.join(map(str, result)))
            return
        return

    for i in range(start, c):
        result.append(arr[i])
        dfs(i + 1)
        result.pop()

arr.sort()
dfs(0)