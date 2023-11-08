import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

result = [0,0]

def check(d):
    for i in range(n):
        cnt = 0
        temp = 0
        for j in range(n):
            status = False
            if d == 'length':
                status = True if arr[i][j] == '.' else False
            else:
                status = True if arr[j][i] == '.' else False

            if status:
                temp += 1
            else:
                if temp >= 2:
                    if d == 'length':
                        result[0] += 1
                    else:
                        result[1] += 1
                temp = 0

            if j == n - 1:
                if temp >= 2:
                    if d == 'length':
                        result[0] += 1
                    else:
                        result[1] += 1

check('length')
check('width')
print(*result)